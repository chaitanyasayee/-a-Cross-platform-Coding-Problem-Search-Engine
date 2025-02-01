import { useState } from 'react';

export interface SearchResult {
  "Challenge Name": string;
  "Question Link": string;
  "Score": number;
}

export const useSearch = () => {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const searchChallenges = async (query: string, platform: string) => {
    if (!query || !platform) return;
    
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch(`/api/${platform.toLowerCase()}?query=${encodeURIComponent(query)}`);
      if (!response.ok) {
        throw new Error('Search failed');
      }
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      setResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  return { results, isLoading, error, searchChallenges };
};
