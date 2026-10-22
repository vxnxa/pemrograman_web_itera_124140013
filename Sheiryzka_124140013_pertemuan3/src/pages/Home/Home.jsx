import { useEffect } from 'react';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';
import { useBooks } from '../../context/BookContext';
import './Home.css';

function Home() {
  const {
    books, filteredBooks, searchQuery, setSearchQuery, filterStatus, setFilterStatus,
    editingBook, setEditingBook, addBook, updateBook, deleteBook,
  } = useBooks();

  // Update judul tab sesuai jumlah buku
  useEffect(() => {
    document.title = `Jejak Halaman (${books.length})`;
  }, [books.length]);

  const handleSubmit = (data) => {
    if (editingBook) {
      updateBook(editingBook.id, data);
      setEditingBook(null);
    } else {
      addBook(data);
    }
  };

  return (
    <section className="home">
      <h2>{editingBook ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
      <BookForm
        onSubmit={handleSubmit}
        editingBook={editingBook}
        onCancel={() => setEditingBook(null)}
      />
      <h2>Daftar Buku</h2>
      <BookFilter
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        status={filterStatus}
        onStatusChange={setFilterStatus}
      />
      <BookList books={filteredBooks} onEdit={setEditingBook} onDelete={deleteBook} />
    </section>
  );
}

export default Home;