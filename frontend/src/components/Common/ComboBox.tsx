import { Box, Input, Text, Portal, Stack } from "@chakra-ui/react";
import { useState, useRef, useEffect } from "react";

const options = [
  { label: "React.js", value: "react" },
  { label: "Vue.js", value: "vue" },
  { label: "Angular", value: "angular" },
  { label: "Svelte", value: "svelte" },
];

export default function ComboBox() {
  const [search, setSearch] = useState("");
  const [selected, setSelected] = useState<string | null>(null);
  const [isOpen, setIsOpen] = useState(false);
  const boxRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (boxRef.current && !boxRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const filtered = options.filter((opt) =>
    opt.label.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <Stack
      maxW="300px"
      mx="auto"
      mt={6}
      ref={boxRef}
      position="relative"
    >
      <Input
        placeholder="Search framework..."
        value={search}
        onFocus={() => setIsOpen(true)}
        onChange={(e) => {
          setSearch(e.target.value);
          setIsOpen(true);
        }}
      />

      {isOpen && filtered.length > 0 && (
        <Box
          position="absolute"
          top="100%"
          left={0}
          right={0}
          mt={1}
          border="1px solid"
          borderColor="gray.200"
          borderRadius="md"
          bg="white"
          zIndex={10}
        >
          {filtered.map((item) => (
            <Box
              key={item.value}
              px={4}
              py={2}
              _hover={{ bg: "gray.100", cursor: "pointer" }}
              onClick={() => {
                setSelected(item.label);
                setSearch(item.label);
                setIsOpen(false);
              }}
            >
              {item.label}
            </Box>
          ))}
        </Box>
      )}

      {selected && (
        <Text fontSize="sm" color="gray.600">
          Selected: {selected}
        </Text>
      )}
    </Stack>
  );
}
