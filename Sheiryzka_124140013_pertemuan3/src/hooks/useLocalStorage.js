import { useState, useEffect } from 'react';

// Hook untuk menyimpan state ke localStorage secara persisten
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  // Simpan ulang setiap kali value berubah
  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Gagal menyimpan ke localStorage:', error);
    }
  }, [key, value]);

  return [value, setValue];
}

export default useLocalStorage;