import React from "react";
import { withMainlayout } from "../layouts";
import { DashboardView } from "../components/Views/Dashboard";

export const Dashboard: React.FC = withMainlayout(() => {
  return <DashboardView />;
});
