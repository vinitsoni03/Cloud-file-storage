import { useState, useCallback } from 'react';
import { getFiles } from '../api/apiClient';

interface FileItem {
  key: string;
  url: string;
}

export const useFiles = () => {
  const [files, setFiles] = useState<FileItem[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchFiles = useCallback(async () => {
    setIsLoading(true);
    setError(null);

    try {
      const filesData = await getFiles();
      setFiles(filesData);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load files');
    } finally {
      setIsLoading(false);
    }
  }, []);

  return { files, fetchFiles, isLoading, error };
};
