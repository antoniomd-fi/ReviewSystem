'use client';

import { useEffect, useState } from 'react';
import api from './utils/api';
import BusinessCard from './components/BusinessCard';
import { Business } from './types';
import BusinessDetails from './components/BusinessDetails';

export default function Page() {
  const [businesses, setBusinesses] = useState<Business[]>([]);
  const [filteredBusinesses, setFilteredBusinesses] = useState<Business[]>([]);
  const [selectedBusiness, setSelectedBusiness] = useState<Business | null>(null);
  const [isPanelVisible, setIsPanelVisible] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    async function fetchBusinesses() {
      try {
        const response = await api.get('/businesses/');
        setBusinesses(response.data);
        setFilteredBusinesses(response.data);
      } catch (error) {
        console.error('Error fetching businesses:', error);
      }
    }

    fetchBusinesses();
  }, []);

  const handleSelectBusiness = (business: Business) => {
    setSelectedBusiness(business);
    setIsPanelVisible(true);
  };

  const handleClosePanel = () => {
    setIsPanelVisible(false);
    setSelectedBusiness(null);
  };

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const term = event.target.value;
    setSearchTerm(term);

    if (term) {
      const filtered = businesses.filter(business =>
        business.name.toLowerCase().includes(term.toLowerCase())
      );
      setFilteredBusinesses(filtered);
    } else {
      setFilteredBusinesses(businesses);
    }
  };

  return (
    <div className="d-flex">
      <div style={{ width: '40%', overflowY: 'auto', height: '100vh', padding: '20px' }}>
        <input
          type="text"
          placeholder="Search Business..."
          value={searchTerm}
          onChange={handleSearchChange}
          className="search-bar"
        />
        {filteredBusinesses.map((business) => (
          <BusinessCard
            key={business.id}
            business={business}
            onSelectBusiness={handleSelectBusiness}
          />
        ))}
      </div>

      {/* Panel lateral con animación */}
      <div className={`side-panel ${isPanelVisible ? 'visible' : ''}`}>
        <button className="close-button" onClick={handleClosePanel}>×</button>
        {selectedBusiness && (
          <BusinessDetails business={selectedBusiness} />
        )}
      </div>

      <style jsx>{`
        .side-panel {
          position: fixed;
          right: -100%;
          top: 0;
          width: 60%;
          height: 100vh;
          background-color: white;
          box-shadow: -4px 0 8px rgba(0, 0, 0, 0.2);
          transition: right 0.4s ease;
          padding: 20px;
          z-index: 1000;
        }

        .side-panel.visible {
          right: 0;
        }

        .close-button {
          position: absolute;
          top: 10px;
          right: 10px;
          background: transparent;
          border: none;
          font-size: 24px;
          cursor: pointer;
          color: #333;
          transition: color 0.2s;
        }

        .close-button:hover {
          color: #ff4d4d;
        }

        .search-bar {
          width: 100%;
          padding: 10px;
          margin-bottom: 20px;
          font-size: 14px;
          border: 1px solid #ccc;
          border-radius: 5px;
        }

        .search-bar:focus {
          outline: none;
          border-color: #80bdff;
          box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
        }
      `}</style>
    </div>
  );
}
