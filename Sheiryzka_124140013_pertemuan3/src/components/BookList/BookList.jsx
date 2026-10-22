import PropTypes from 'prop-types';
import './BookList.css';

const STATUS_LABEL = { milik: 'Dimiliki', baca: 'Sedang Dibaca', beli: 'Ingin Dibeli' };

const bookShape = PropTypes.shape({
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
  status: PropTypes.string.isRequired,
});

function BookItem({ book, onEdit, onDelete }) {
  return (
    <li className="book-item">
      <div>
        <strong>{book.title}</strong>
        <p>{book.author}</p>
        <span className={`badge badge-${book.status}`}>{STATUS_LABEL[book.status]}</span>
      </div>
      <div className="item-actions">
        <button onClick={() => onEdit(book)}>Edit</button>
        <button className="danger" onClick={() => onDelete(book.id)}>Hapus</button>
      </div>
    </li>
  );
}

BookItem.propTypes = {
  book: bookShape.isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

function BookList({ books, onEdit, onDelete }) {
  if (books.length === 0) {
    return <p className="empty">Belum ada buku yang cocok.</p>;
  }
  return (
    <ul className="book-list">
      {books.map((book) => (
        <BookItem key={book.id} book={book} onEdit={onEdit} onDelete={onDelete} />
      ))}
    </ul>
  );
}

BookList.propTypes = {
  books: PropTypes.arrayOf(bookShape).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

export default BookList;