import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://api.example.com/prod';

export const getPresignedUploadUrl = async (fileName: string) => {
  const response = await axios.post(`${API_BASE_URL}/upload`, { fileName });
  return response.data;
};

export const uploadFileToS3 = async (url: string, file: File) => {
  await axios.put(url, file, {
    headers: {
      'Content-Type': file.type
    }
  });
};

export const getFiles = async () => {
  const response = await axios.get(`${API_BASE_URL}/files`);
  return response.data.files;
};
