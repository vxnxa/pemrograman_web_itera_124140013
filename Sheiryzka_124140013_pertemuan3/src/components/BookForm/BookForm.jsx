import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './BookForm.css';

function BookForm({ onSubmit, editingBook, onCancel }) {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('milik');
  const [errors, setErrors] = useState({});

  // Isi form saat mode edit, kosongkan saat selesai
  useEffect(() => {
    if (editingBook) {
      setTitle(editingBook.title);
      setAuthor(editingBook.author);
      setStatus(editingBook.status);
    } else {
      setTitle('');
      setAuthor('');
      setStatus('milik');
    }
    setErrors({});
  }, [editingBook]);

  // Validasi kolom wajib isi
  const validate = () => {
    const newErrors = {};
    if (!title.trim()) newErrors.title = 'Judul wajib diisi';
    if (!author.trim()) newErrors.author = 'Penulis wajib diisi';
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = validate();
    setErrors(newErrors);
    if (Object.keys(newErrors).length > 0) return;
    onSubmit({ title: title.trim(), author: author.trim(), status });
  };

  return (
    <form className="book-form" onSubmit={handleSubmit} noValidate>
      <div className="field">
        <label htmlFor="title">Judul</label>
        <input
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className={errors.title ? 'input-error' : ''}
        />
        {errors.title && <span className="error-text">{errors.title}</span>}
      </div>

      <div className="field">
        <label htmlFor="author">Penulis</label>
        <input
          id="author"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          className={errors.author ? 'input-error' : ''}
        />
        {errors.author && <span className="error-text">{errors.author}</span>}
      </div>

      <div className="field">
        <label htmlFor="status">Status</label>
        <select id="status" value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="milik">Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
      </div>

      <div className="actions">
        <button type="submit">{editingBook ? 'Simpan Perubahan' : 'Tambah Buku'}</button>
        {editingBook && (
          <button type="button" className="secondary" onClick={onCancel}>Batal</button>
        )}
      </div>
    </form>
  );
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  editingBook: PropTypes.shape({
    id: PropTypes.string,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.string,
  }),
  onCancel: PropTypes.func,
};

BookForm.defaultProps = { editingBook: null, onCancel: () => {} };

export default BookForm;