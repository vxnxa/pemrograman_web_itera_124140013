import PropTypes from 'prop-types';
import './BookFilter.css';

function BookFilter({ searchQuery, onSearchChange, status, onStatusChange }) {
  return (
    <div className="book-filter">
      <input
        type="search"
        placeholder="Cari judul atau penulis..."
        value={searchQuery}
        onChange={(e) => onSearchChange(e.target.value)}
        aria-label="Cari buku"
      />
      <select
        value={status}
        onChange={(e) => onStatusChange(e.target.value)}
        aria-label="Filter status"
      >
        <option value="semua">Semua</option>
        <option value="milik">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
    </div>
  );
}

BookFilter.propTypes = {
  searchQuery: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  status: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
};

export default BookFilter;