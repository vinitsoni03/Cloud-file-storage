import React, { useEffect } from 'react';
import { useFiles } from '../hooks/useFiles';

const FileList: React.FC = () => {
  const { files, fetchFiles, isLoading, error } = useFiles();

  useEffect(() => {
    fetchFiles();
  }, [fetchFiles]);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="file-list">
      <h2>Your Files</h2>
      <ul>
        {files.map((file) => (
          <li key={file.key}>
            <a href={file.url} target="_blank" rel="noopener noreferrer">
              {file.key}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FileList;
