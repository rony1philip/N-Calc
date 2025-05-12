import { Box, Container, Text } from "@chakra-ui/react";
import { createFileRoute } from "@tanstack/react-router";
import useAuth from "@/hooks/useAuth";
import ComboBox from "@/components/Common/ComboBox";

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
});

function Dashboard() {
  const { user: currentUser } = useAuth();
  console.log("MAIN LOADED!");

  return (
    <>
      <Container maxW="full">
        <Box pt={12} m={4}>
          <Text fontSize="2xl" truncate maxW="sm">
            Hi, {currentUser?.full_name || currentUser?.email} 👋🏼
          </Text>
          <Text>Welcome backfffff, nice to see you again!</Text>
        </Box>
        <Box>
          <ComboBox></ComboBox>
        </Box>
      </Container>
    </>
  );
}
