import api from './Api';

export const predict= async (features) => {
  try {
    const response = await api.post('/predict', { features });
    return response.data;
  } catch (error) {

    const msg = error.response?.data?.detail || error.message;
    throw new Error(msg);
  }
};