import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, renderHook, act } from '@testing-library/react';
import BookForm from '../components/BookForm/BookForm';
import BookList from '../components/BookList/BookList';
import BookFilter from '../components/BookFilter/BookFilter';
import useBookStats from '../hooks/useBookStats';
import useLocalStorage from '../hooks/useLocalStorage';

const sampleBooks = [
  { id: '1', title: 'Laskar Pelangi', author: 'Andrea Hirata', status: 'milik' },
  { id: '2', title: 'Bumi', author: 'Tere Liye', status: 'baca' },
  { id: '3', title: 'Dilan 1990', author: 'Pidi Baiq', status: 'beli' },
  { id: '4', title: 'Negeri 5 Menara', author: 'A. Fuadi', status: 'milik' },
];

describe('BookForm', () => {
  it('menampilkan pesan error saat input kosong', () => {
    const onSubmit = vi.fn();
    render(<BookForm onSubmit={onSubmit} />);
    fireEvent.click(screen.getByRole('button', { name: /tambah buku/i }));
    expect(screen.getByText('Judul wajib diisi')).toBeInTheDocument();
    expect(screen.getByText('Penulis wajib diisi')).toBeInTheDocument();
    expect(onSubmit).not.toHaveBeenCalled();
  });

  it('memanggil onSubmit dengan data valid', () => {
    const onSubmit = vi.fn();
    render(<BookForm onSubmit={onSubmit} />);
    fireEvent.change(screen.getByLabelText(/judul/i), { target: { value: 'Laskar Pelangi' } });
    fireEvent.change(screen.getByLabelText(/penulis/i), { target: { value: 'Andrea Hirata' } });
    fireEvent.click(screen.getByRole('button', { name: /tambah buku/i }));
    expect(onSubmit).toHaveBeenCalledWith({
      title: 'Laskar Pelangi',
      author: 'Andrea Hirata',
      status: 'milik',
    });
  });
});

describe('BookList', () => {
  it('menampilkan pesan kosong jika tidak ada buku', () => {
    render(<BookList books={[]} onEdit={() => {}} onDelete={() => {}} />);
    expect(screen.getByText(/belum ada buku/i)).toBeInTheDocument();
  });

  it('memanggil onDelete dengan id yang benar', () => {
    const onDelete = vi.fn();
    render(<BookList books={[sampleBooks[0]]} onEdit={() => {}} onDelete={onDelete} />);
    expect(screen.getByText('Laskar Pelangi')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: /hapus/i }));
    expect(onDelete).toHaveBeenCalledWith('1');
  });
});

describe('BookFilter', () => {
  it('memanggil onSearchChange saat mengetik', () => {
    const onSearchChange = vi.fn();
    render(
      <BookFilter
        searchQuery=""
        onSearchChange={onSearchChange}
        status="semua"
        onStatusChange={() => {}}
      />
    );
    fireEvent.change(screen.getByLabelText('Cari buku'), { target: { value: 'bumi' } });
    expect(onSearchChange).toHaveBeenCalledWith('bumi');
  });
});

describe('Custom hooks', () => {
  beforeEach(() => localStorage.clear());

  it('useBookStats menghitung statistik dengan benar', () => {
    const { result } = renderHook(() => useBookStats(sampleBooks));
    expect(result.current).toEqual({ total: 4, milik: 2, baca: 1, beli: 1 });
  });

  it('useLocalStorage menyimpan nilai ke localStorage', () => {
    const { result } = renderHook(() => useLocalStorage('test-key', []));
    act(() => result.current[1](['a']));
    expect(JSON.parse(localStorage.getItem('test-key'))).toEqual(['a']);
  });
});