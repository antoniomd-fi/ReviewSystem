import { Business } from '../types';
import ReviewForm from './ReviewForm';

type BusinessDetailsProps = {
  business: Business;
};

export default function BusinessDetails({ business }: BusinessDetailsProps) {
  return (
    <div>
      <h2>{business.name}</h2>
      <p>Email: {business.email}</p>
      <ReviewForm businessId={business.id} onReviewSubmitted={() => alert('Review submitted!')} />
    </div>
  );
}