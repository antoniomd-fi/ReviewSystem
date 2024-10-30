// import { Business } from '../types';

// type BusinessCardProps = {
//   business: Business;
//   onSelectBusiness: (business: Business) => void;
// };

// export default function BusinessCard({ business, onSelectBusiness }: BusinessCardProps) {
//   return (
//     <div
//       className="card my-3"
//       onClick={() => onSelectBusiness(business)}
//       style={{ cursor: 'pointer' }}
//     >
//       <div className="card-body">
//         <h5 className="card-title">{business.name}</h5>
//         <p className="card-text">Rating: {business.rating}⭐</p>
//       </div>
//     </div>
//   );
// }

import { Business } from '../types';

type BusinessCardProps = {
    business: Business;
    onSelectBusiness: (business: Business) => void;
};

export default function BusinessCard({ business, onSelectBusiness }: BusinessCardProps) {
    return (
        <div className="business-card" onClick={() => onSelectBusiness(business)}>
            <h5 className="business-name">{business.name}</h5>
            <p className="business-rating">
                Rating: <span className="star">★</span>
            </p>
            <style jsx>{`
                .business-card {
                    padding: 15px;
                    margin: 10px 5px;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    transition: transform 0.2s;
                    cursor: pointer;
                }

                .business-card:hover {
                    transform: scale(1.02);
                }

                .business-name {
                    margin: 0;
                    font-size: 18px;
                    color: #333;
                }

                .business-rating {
                    font-size: 16px;
                    color: #888;
                }

                .star {
                    color: #ffbf00;
                    font-size: 18px;
                }
            `}</style>
        </div>
    );
}
