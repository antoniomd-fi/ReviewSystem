import { useState } from 'react';
import api from '../utils/api';

type ReviewFormProps = {
    businessId: number;
    onReviewSubmitted: () => void;
};

export default function ReviewForm({ businessId, onReviewSubmitted }: ReviewFormProps) {
    const [rating, setRating] = useState<number>(0);
    const [comment, setComment] = useState<string>('');

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        try {
            await api.post('/reviews/', {
                business: businessId,
                rating,
                comment,
                user: 1,
            });
            onReviewSubmitted();
            setRating(0);
            setComment('');
        } catch (error) {
            console.error('Error submitting review:', error);
        }
    };

    const handleStarClick = (value: number) => {
        setRating(value);
    };

    return (
        <form onSubmit={handleSubmit} className="review-form">
            <div className="rating">
                {[1, 2, 3, 4, 5].map((star) => (
                    <span
                        key={star}
                        className={`star ${star <= rating ? 'filled' : ''}`}
                        onClick={() => handleStarClick(star)}
                    >
                        ★
                    </span>
                ))}
            </div>
            <textarea
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                placeholder="Share details of your experience with this place"
                required
                className="comment-box"
            />
            <button type="submit" className="submit-button">Send Review</button>
            <style jsx>{`
                .review-form {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    max-width: 400px;
                    margin-top: 15px;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }

                .rating {
                    display: flex;
                    gap: 10px;
                    font-size: 32px; /* Tamaño de las estrellas */
                    justify-content: center;
                    cursor: pointer;
                }

                .star {
                    color: #e0e0e0;
                    transition: color 0.3s;
                }

                .star.filled {
                    color: #ffbf00; /* Amarillo más agradable */
                }

                .comment-box {
                    width: 100%;
                    height: 100px;
                    padding: 10px;
                    font-size: 14px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    resize: none;
                }

                .comment-box:focus {
                    outline: none;
                    border-color: #80bdff;
                    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
                }

                .submit-button {
                    background-color: #007bff;
                    color: #fff;
                    padding: 10px 15px;
                    font-size: 14px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }

                .submit-button:hover {
                    background-color: #0056b3;
                }
            `}</style>
        </form>
    );
}