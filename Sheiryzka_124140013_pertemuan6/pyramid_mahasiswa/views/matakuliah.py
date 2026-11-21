from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Matakuliah


_REQUIRED_FIELDS = ("kode_mk", "nama_mk", "sks", "semester")


def _read_json_object(request):
    try:
        payload = request.json_body
    except (ValueError, UnicodeDecodeError):
        raise HTTPBadRequest(json_body={"error": "Body harus berupa JSON yang valid."})

    if not isinstance(payload, dict):
        raise HTTPBadRequest(json_body={"error": "Body JSON harus berupa object."})
    return payload


def _validate_required_fields(payload):
    for field in _REQUIRED_FIELDS:
        value = payload.get(field)
        if value is None:
            return f"Field {field} wajib diisi."
        if field in ("kode_mk", "nama_mk") and (
            not isinstance(value, str) or not value.strip()
        ):
            return f"Field {field} harus berupa teks dan tidak boleh kosong."

    for field in ("sks", "semester"):
        value = payload[field]
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            return f"Field {field} harus berupa bilangan bulat positif."

    return None


def _find_by_id(request):
    return (
        request.dbsession.query(Matakuliah)
        .filter_by(id=int(request.matchdict["id"]))
        .first()
    )


@view_config(route_name="matakuliah_list", request_method="GET", renderer="json")
def matakuliah_list(request):
    courses = (
        request.dbsession.query(Matakuliah)
        .order_by(Matakuliah.id.asc())
        .all()
    )
    return {"matakuliah": [course.to_dict() for course in courses]}


@view_config(route_name="matakuliah_detail", request_method="GET", renderer="json")
def matakuliah_detail(request):
    course = _find_by_id(request)
    if course is None:
        return HTTPNotFound(
            json_body={"error": "Mata kuliah tidak ditemukan."}
        )
    return {"matakuliah": course.to_dict()}


@view_config(route_name="matakuliah_add", request_method="POST", renderer="json")
def matakuliah_add(request):
    payload = _read_json_object(request)
    error = _validate_required_fields(payload)
    if error:
        return HTTPBadRequest(json_body={"error": error})

    dbsession = request.dbsession
    duplicate = (
        dbsession.query(Matakuliah)
        .filter_by(kode_mk=payload["kode_mk"].strip())
        .first()
    )
    if duplicate is not None:
        return HTTPBadRequest(json_body={"error": "kode_mk sudah digunakan."})

    course = Matakuliah(
        kode_mk=payload["kode_mk"].strip(),
        nama_mk=payload["nama_mk"].strip(),
        sks=payload["sks"],
        semester=payload["semester"],
    )
    dbsession.add(course)
    dbsession.flush()
    return {"success": True, "matakuliah": course.to_dict()}


@view_config(route_name="matakuliah_update", request_method="PUT", renderer="json")
def matakuliah_update(request):
    course = _find_by_id(request)
    if course is None:
        return HTTPNotFound(
            json_body={"error": "Mata kuliah tidak ditemukan."}
        )

    payload = _read_json_object(request)

    for field in ("kode_mk", "nama_mk"):
        if field in payload:
            value = payload[field]
            if not isinstance(value, str) or not value.strip():
                return HTTPBadRequest(
                    json_body={"error": f"Field {field} tidak boleh kosong."}
                )
            payload[field] = value.strip()

    for field in ("sks", "semester"):
        if field in payload:
            value = payload[field]
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                return HTTPBadRequest(
                    json_body={
                        "error": f"Field {field} harus berupa bilangan bulat positif."
                    }
                )

    if "kode_mk" in payload:
        duplicate = (
            request.dbsession.query(Matakuliah)
            .filter(
                Matakuliah.kode_mk == payload["kode_mk"],
                Matakuliah.id != course.id,
            )
            .first()
        )
        if duplicate is not None:
            return HTTPBadRequest(json_body={"error": "kode_mk sudah digunakan."})

    for field in _REQUIRED_FIELDS:
        if field in payload:
            setattr(course, field, payload[field])

    return {"success": True, "matakuliah": course.to_dict()}


@view_config(
    route_name="matakuliah_delete", request_method="DELETE", renderer="json"
)
def matakuliah_delete(request):
    course = _find_by_id(request)
    if course is None:
        return HTTPNotFound(
            json_body={"error": "Mata kuliah tidak ditemukan."}
        )

    request.dbsession.delete(course)
    return {
        "success": True,
        "message": f"Mata kuliah {course.kode_mk} berhasil dihapus.",
    }
