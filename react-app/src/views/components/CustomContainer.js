import { Box, Container } from "@mui/system";

function CustomContainer({ children }) {
  return (
    <Box
      sx={{
        width: "100%",
        height: "100vh",
        position: "relative",
      }}
    >
      <Box
        component="img"
        sx={{
          height: "100%",
          width: "auto",
          minWidth: "100%",
          position: "fixed",
        }}
        alt="Background"
        src="/static/images/bg.jpg"
      />
      <Box
        sx={{
          height: "100%",
          width: "100%",
          position: "fixed",
          backgroundColor: "#000000a3",
        }}
      />
      <Container
        sx={{
          position: "relative",
          py: "9rem",
        }}
        maxWidth="sm"
      >
        {children}
      </Container>
    </Box>
  );
}

export default CustomContainer;
