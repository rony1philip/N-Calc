import { Box, Container, Text } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"
import { Combobox } from "/Users/ronyphilip/Desktop/N-CALC/N-Calc/frontend/src/components/Common/combobox";
import useAuth from "@/hooks/useAuth"

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
})

function Dashboard() {
  const { user: currentUser } = useAuth()

  return (
    <>
      <Container maxW="full">
        <Box pt={12} m={4}>
          <Text fontSize="2xl" truncate maxW="sm">
            Hi, {currentUser?.full_name || currentUser?.email} 👋🏼
           
          </Text>
          <Text>Welcome back, nice to see you again!</Text>
          <Combobox></Combobox>
        </Box>

      </Container>
    </>
  )
}
