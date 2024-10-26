import { EventTable } from "../Common";

export const DashboardView: React.FC = () => {
  return (
    <>
      <div className="flex-col w-full h-full p-16">
        <div className="flex justify-end pb-4">
          <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
            New Event
          </button>
        </div>
        <div className="flex w-full h-full">
          <EventTable />
        </div>
      </div>
    </>
  );
};
