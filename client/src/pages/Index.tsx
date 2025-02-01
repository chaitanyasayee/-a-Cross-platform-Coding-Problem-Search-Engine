import { useState, useEffect } from "react";
import { SearchBar } from "@/components/SearchBar";
import { PlatformFilter } from "@/components/PlatformFilter";
import { ChallengeCard } from "@/components/ChallengeCard";
import { ChallengeSkeleton } from "@/components/ChallengeSkeleton";
import { Code2 } from "lucide-react";
import { useSearch, SearchResult } from "@/hooks/useSearch";
import { useToast } from "@/components/ui/use-toast";

const platforms = [
  { id: "leetcode", name: "LeetCode" },
  { id: "codechef", name: "CodeChef" },
  { id: "codeforces", name: "CodeForces" },
];

export interface Challenge {
  id: string;
  title: string;
  platform: string;
  difficulty: string;
  url: string;
  score?: number;
}

const getDifficulty = (score: number): "easy" | "medium" | "hard" => {
  if (score < 1) return "easy";
  if (score < 2) return "medium";
  return "hard";
};

const Index = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedPlatform, setSelectedPlatform] = useState<string>("leetcode");
  const { results, isLoading, error, searchChallenges } = useSearch();
  const { toast } = useToast();

  useEffect(() => {
    if (error) {
      toast({
        variant: "destructive",
        title: "Error",
        description: error
      });
    }
  }, [error, toast]);

  const transformResults = (results: SearchResult[]): Challenge[] => {
    return results.map((result, index) => ({
      id: index.toString(),
      title: result["Challenge Name"],
      platform: selectedPlatform,
      difficulty: getDifficulty(result.Score),
      url: result["Question Link"],
      score: result.Score
    }));
  };

  const handleSearch = async (query: string) => {
    setSearchQuery(query);
    if (query.trim()) {
      await searchChallenges(query, selectedPlatform);
    }
  };

  const handlePlatformChange = async (platform: string) => {
    setSelectedPlatform(platform);
    if (searchQuery.trim()) {
      await searchChallenges(searchQuery, platform);
    }
  };

  return (
    <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-background to-secondary/50">
      <div className="max-w-7xl mx-auto space-y-12">
        <div className="text-center space-y-8">
          <div className="flex items-center justify-center gap-3 animate-fade-in">
            <Code2 className="w-12 h-12 text-primary" />
            <h1 className="text-4xl sm:text-5xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-primary to-purple-400">
              Find Your Next Coding Challenge
            </h1>
          </div>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto animate-fade-in">
            Search across LeetCode, CodeChef, and CodeForces to find the perfect
            programming challenge for your skill level.
          </p>
          <SearchBar onSearch={handleSearch} />
        </div>

        <div className="space-y-8 animate-fade-in">
          <PlatformFilter
            platforms={platforms}
            selectedPlatform={selectedPlatform}
            onSelect={handlePlatformChange}
          />

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {isLoading ? (
              <>
                <ChallengeSkeleton />
                <ChallengeSkeleton />
                <ChallengeSkeleton />
              </>
            ) : results.length > 0 ? (
              transformResults(results).map((challenge) => (
                <ChallengeCard 
                  key={challenge.id} 
                  challenge={challenge}
                />
              ))
            ) : (
              <div className="col-span-full text-center text-muted-foreground">
                {searchQuery ? "No results found" : "Start searching to see challenges"}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
