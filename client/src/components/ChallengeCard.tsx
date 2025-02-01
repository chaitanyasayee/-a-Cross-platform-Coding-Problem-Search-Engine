import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ExternalLink } from "lucide-react";
import { Challenge } from "@/pages/Index";

interface ChallengeCardProps {
  challenge: Challenge;
}

export const ChallengeCard = ({ challenge }: ChallengeCardProps) => {
  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case 'easy':
        return 'bg-green-500/10 text-green-500';
      case 'medium':
        return 'bg-yellow-500/10 text-yellow-500';
      case 'hard':
        return 'bg-red-500/10 text-red-500';
      default:
        return 'bg-gray-500/10 text-gray-500';
    }
  };

  return (
    <Card className="transition-all hover:shadow-lg">
      <CardHeader>
        <div className="flex justify-between items-start">
          <CardTitle className="text-lg font-semibold">{challenge.title}</CardTitle>
          <Badge variant="outline" className={getDifficultyColor(challenge.difficulty)}>
            {challenge.difficulty}
          </Badge>
        </div>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="flex flex-col gap-2">
          <Badge variant="secondary">{challenge.platform}</Badge>
          {challenge.score !== undefined && (
            <span className="text-sm text-muted-foreground">
              Match Score: {challenge.score.toFixed(2)}
            </span>
          )}
        </div>
        <Button 
          variant="outline" 
          className="w-full"
          onClick={() => window.open(challenge.url, '_blank')}
        >
          Solve Challenge <ExternalLink className="ml-2 h-4 w-4" />
        </Button>
      </CardContent>
    </Card>
  );
};
