import { Toaster } from "react-hot-toast";
import { AuthProvider } from "./context";
import AppRouter from "./router/AppRouter";

function App() {
  return (
    <AuthProvider>
      <AppRouter />
      <Toaster position="bottom-center" />
    </AuthProvider>
  );
}

export default App;
