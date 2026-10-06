// ambil data keranjang dari localStorage, kalau belum ada pakai array kosong
let keranjang = JSON.parse(localStorage.getItem("keranjang")) || [];

const form = document.getElementById("form-barang");
const inputNama = document.getElementById("nama");
const inputHarga = document.getElementById("harga");
const inputjumlah = document.getElementById("jumlah");
const inputPromo = document.getElementById("promo");
const inputBayar = document.getElementById("bayar");
const isiKeranjang = document.getElementById("isi-keranjang");

function formatRupiah(angka) {
  return "Rp " + angka.toLocaleString("id-ID");
}

function simpanKeranjang() {
  localStorage.setItem("keranjang", JSON.stringify(keranjang));
}

// ---------- validasi ----------

function validasiForm() {
  let valid = true;
  const nama = inputNama.value.trim();
  const harga = parseFloat(inputHarga.value);
  const jumlah = parseFloat(inputjumlah.value);

  if (nama.length < 3) {
    tampilError(inputNama, "error-nama", "Nama barang minimal 3 karakter.");
    valid = false;
  } else {
    tampilError(inputNama, "error-nama", "");
  }

  if (isNaN(harga)) {
    tampilError(inputHarga, "error-harga", "Harga wajib diisi dengan angka.");
    valid = false;
  } else if (harga < 500) {
    tampilError(inputHarga, "error-harga", "Harga minimal Rp 500.");
    valid = false;
  } else {
    tampilError(inputHarga, "error-harga", "");
  }

  if (isNaN(jumlah)) {
    tampilError(inputjumlah, "error-jumlah", "Jumlah wajib diisi dengan angka.");
    valid = false;
  } else if (!Number.isInteger(jumlah) || jumlah < 1) {
    tampilError(inputjumlah, "error-jumlah", "Jumlah harus bilangan bulat minimal 1.");
    valid = false;
  } else {
    tampilError(inputjumlah, "error-jumlah", "");
  }

  return valid;
}

function tampilError(input, idError, pesan) {
  document.getElementById(idError).textContent = pesan;
  if (pesan === "") {
    input.classList.remove("salah");
  } else {
    input.classList.add("salah");
  }
}

// ---------- hitung ----------

function hitungTotal() {
  let total = 0;
  for (const item of keranjang) {
    total += item.harga * item.jumlah;
  }
  return total;
}

function hitungDiskon(total) {
  const info = document.getElementById("info-diskon");
  const kode = inputPromo.value.trim().toUpperCase();

  if (total >= 50000) {
    info.textContent = "Belanja minimal Rp 50.000, diskon 10%.";
    return total * 0.1;
  }
  if (kode === "HEMAT10" && total > 0) {
    info.textContent = "Kode HEMAT10 dipakai, diskon 10%.";
    return total * 0.1;
  }
  if (kode !== "") {
    info.textContent = "Kode promo tidak valid.";
  } else {
    info.textContent = "Diskon 10% untuk belanja min. Rp 50.000 atau kode HEMAT10.";
  }
  return 0;
}

function hitungKembalian(totalAkhir) {
  const el = document.getElementById("kembalian");
  const bayar = parseFloat(inputBayar.value);

  if (isNaN(bayar)) {
    el.textContent = "";
    return;
  }

  const kembalian = bayar - totalAkhir;
  if (totalAkhir === 0) {
    el.textContent = "Keranjang masih kosong.";
    el.className = "merah";
  } else if (kembalian < 0) {
    el.textContent = "Uang belum mencukupi, kurang " + formatRupiah(-kembalian);
    el.className = "merah";
  } else {
    el.textContent = "Kembalian: " + formatRupiah(kembalian);
    el.className = "hijau";
  }
}

// ---------- tampilan ----------

function tampilkanKeranjang() {
  if (keranjang.length === 0) {
    isiKeranjang.innerHTML = `<tr><td colspan="6" class="kosong">Keranjang masih kosong</td></tr>`;
    return;
  }

  isiKeranjang.innerHTML = "";
  keranjang.forEach(function (item, index) {
    // replace < supaya nama barang tidak dibaca sebagai tag html
    const nama = item.nama.replace(/</g, "&lt;");
    isiKeranjang.innerHTML += `
      <tr>
        <td>${index + 1}</td>
        <td>${nama}</td>
        <td class="angka">${formatRupiah(item.harga)}</td>
        <td class="angka">${item.jumlah}</td>
        <td class="angka">${formatRupiah(item.harga * item.jumlah)}</td>
        <td><button class="hapus" data-index="${index}">Hapus</button></td>
      </tr>
    `;
  });
}

function tampilkanSemua() {
  tampilkanKeranjang();

  const total = hitungTotal();
  const diskon = hitungDiskon(total);
  const totalAkhir = total - diskon;

  document.getElementById("total").textContent = formatRupiah(total);
  document.getElementById("diskon").textContent = "- " + formatRupiah(diskon);
  document.getElementById("total-akhir").textContent = formatRupiah(totalAkhir);

  hitungKembalian(totalAkhir);
}

// ---------- event ----------

form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (!validasiForm()) {
    return; // ada yang salah, jangan masuk keranjang
  }

  keranjang.push({
    nama: inputNama.value.trim(),
    harga: parseFloat(inputHarga.value),
    jumlah: parseFloat(inputjumlah.value),
  });
  simpanKeranjang();
  form.reset();
  tampilkanSemua();
});

isiKeranjang.addEventListener("click", function (e) {
  if (e.target.classList.contains("hapus")) {
    keranjang.splice(e.target.dataset.index, 1);
    simpanKeranjang();
    tampilkanSemua();
  }
});

document.getElementById("btn-reset").addEventListener("click", function () {
  keranjang = [];
  localStorage.removeItem("keranjang");
  inputPromo.value = "";
  inputBayar.value = "";
  tampilkanSemua();
});

inputPromo.addEventListener("input", tampilkanSemua);
inputBayar.addEventListener("input", tampilkanSemua);

// pertama kali halaman dibuka
tampilkanSemua();