import { Button } from "@/components/ui/button";

interface Platform {
  id: string;
  name: string;
}

interface PlatformFilterProps {
  platforms: Platform[];
  selectedPlatform: string;
  onSelect: (platform: string) => void;
}

export const PlatformFilter = ({ platforms, selectedPlatform, onSelect }: PlatformFilterProps) => {
  return (
    <div className="flex flex-wrap gap-2 justify-center">
      {platforms.map((platform) => (
        <Button
          key={platform.id}
          variant={selectedPlatform === platform.id ? "default" : "outline"}
          onClick={() => onSelect(platform.id)}
        >
          {platform.name}
        </Button>
      ))}
    </div>
  );
};
