import { useMemo } from 'react';

// Hook untuk menghitung statistik buku berdasarkan status
function useBookStats(books) {
  return useMemo(() => {
    const count = (status) => books.filter((b) => b.status === status).length;
    return {
      total: books.length,
      milik: count('milik'),
      baca: count('baca'),
      beli: count('beli'),
    };
  }, [books]);
}

export default useBookStats;