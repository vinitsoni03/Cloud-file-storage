import { useState } from 'react';
import { getPresignedUploadUrl, uploadFileToS3 } from '../api/apiClient';

export const useUpload = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const upload = async (file: File) => {
    setIsLoading(true);
    setError(null);

    try {
      const { uploadUrl, fileKey } = await getPresignedUploadUrl(file.name);
      await uploadFileToS3(uploadUrl, file);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Upload failed');
    } finally {
      setIsLoading(false);
    }
  };

  return { upload, isLoading, error };
};
