import { createContext, useContext, useMemo, useState } from 'react';
import PropTypes from 'prop-types';
import useLocalStorage from '../hooks/useLocalStorage';

const BookContext = createContext(null);

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books', []);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterStatus, setFilterStatus] = useState('semua');
  const [editingBook, setEditingBook] = useState(null);

  const addBook = (data) =>
    setBooks((prev) => [...prev, { id: Date.now().toString(), ...data }]);

  const updateBook = (id, data) =>
    setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...data } : b)));

  const deleteBook = (id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id));
    if (editingBook?.id === id) setEditingBook(null);
  };

  // Gabungan filter status + pencarian judul/penulis
  const filteredBooks = useMemo(() => {
    const q = searchQuery.trim().toLowerCase();
    return books.filter((b) => {
      const matchStatus = filterStatus === 'semua' || b.status === filterStatus;
      const matchSearch =
        b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q);
      return matchStatus && matchSearch;
    });
  }, [books, searchQuery, filterStatus]);

  const value = {
    books, filteredBooks,
    searchQuery, setSearchQuery,
    filterStatus, setFilterStatus,
    editingBook, setEditingBook,
    addBook, updateBook, deleteBook,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}

BookProvider.propTypes = { children: PropTypes.node.isRequired };

// eslint-disable-next-line react-refresh/only-export-components
export function useBooks() {
  const ctx = useContext(BookContext);
  if (!ctx) throw new Error('useBooks harus dipakai di dalam BookProvider');
  return ctx;
}