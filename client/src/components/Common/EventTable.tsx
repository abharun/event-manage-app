export const EventTable: React.FC = () => {
  return (
    <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
      <table className="w-full table-fixed text-sm text-left text-gray-800 border">
        <thead className="text-xs uppercase bg-gray-50">
          <tr>
            <th scope="col" className="w-1/12 p-3">
              <div className="flex justify-center">
                <p>No</p>
              </div>
            </th>
            <th scope="col" className="w-1/12 p-3">
              <div className="flex justify-center">
                <p>Title</p>
              </div>
            </th>
            <th scope="col" className="w-1/6 p-3">
              <div className="flex justify-center">
                <p>Organizer</p>
              </div>
            </th>
            <th scope="col" className="w-1/6 p-3">
              <div className="flex justify-center">
                <p>DateTime</p>
              </div>
            </th>
            <th scope="col" className="w-1/4 p-3">
              <div className="flex justify-center">
                <p>Duration</p>
              </div>
            </th>
            <th scope="col" className="w-1/6 p-3">
              <div className="flex justify-center">
                <p>Location</p>
              </div>
            </th>
            <th scope="col" className="w-1/12" />
          </tr>
        </thead>
        <tbody className="text-center">
          <tr>
            <th className="p-4">1</th>
            <td className="p-4">Event 1</td>
            <td className="p-4">Dash</td>
            <td className="p-4">2000-01-01 08-00-00</td>
            <td className="p-4">2000-01-03 08-00-00(3 days)</td>
            <td className="p-4">Brussels, BE</td>
            <td className="p-4">
              <button className="border-2 border-green-600 p-2 text-green-600 rounded-lg">Join</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};
