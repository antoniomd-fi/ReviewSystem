export type Business = {
    id: number;
    name: string;
    email: string;
    phone_number: string;
    rating?: number; // Puede ser undefined si no tiene reviews
};

export type Review = {
    business: number;
    user: number;
    rating: number;
    comment: string;
};
