'use client';

import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import api from '../../utils/api';
import BusinessDetails from '../../components/BusinessDetails';
import ReviewForm from '../../components/ReviewForm';
import { Business } from '../../types';

export default function BusinessPage() {
    const { id } = useParams();
    const [business, setBusiness] = useState<Business | null>(null);

    const fetchBusiness = async () => {
        try {
            const response = await api.get(`/businesses/${id}`);
            setBusiness(response.data);
        } catch (error) {
            console.error('Error fetching business:', error);
        }
    };

    const handleReviewSubmitted = async () => {
        alert('Review submitted!');
        await fetchBusiness();
    };

    useEffect(() => {
        fetchBusiness();
    }, [id]);

    return (
        <div>
            {business && (
                <>
                    <BusinessDetails business={business} />
                    <ReviewForm businessId={business.id} onReviewSubmitted={handleReviewSubmitted} />
                </>
            )}
        </div>
    );
}