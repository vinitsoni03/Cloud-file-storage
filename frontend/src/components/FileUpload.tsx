import React, { useState } from 'react';
import { useUpload } from '../hooks/useUpload';

const FileUpload: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const { upload, isLoading, error } = useUpload();

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (selectedFile) {
      await upload(selectedFile);
      setSelectedFile(null);
    }
  };

  return (
    <div className="file-upload">
      <h2>Upload File</h2>
      <input type="file" onChange={handleFileChange} />
      {selectedFile && (
        <div>
          <p>Selected: {selectedFile.name}</p>
          <button onClick={handleUpload} disabled={isLoading}>
            {isLoading ? 'Uploading...' : 'Upload'}
          </button>
        </div>
      )}
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default FileUpload;
