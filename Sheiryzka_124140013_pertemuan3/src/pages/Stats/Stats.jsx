import { useBooks } from '../../context/BookContext';
import useBookStats from '../../hooks/useBookStats';
import './Stats.css';

function Stats() {
  const { books } = useBooks();
  const stats = useBookStats(books);

  const items = [
    { label: 'Total Buku', value: stats.total },
    { label: 'Dimiliki', value: stats.milik },
    { label: 'Sedang Dibaca', value: stats.baca },
    { label: 'Ingin Dibeli', value: stats.beli },
  ];

  return (
    <section>
      <h2>Statistik Buku</h2>
      <div className="stats-grid">
        {items.map((item) => (
          <div key={item.label} className="stat-card">
            <span className="stat-value">{item.value}</span>
            <span>{item.label}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Stats;