function Status({ fullName, title, avatarUrl, isActive }) {
  return (
    <div className="flex gap-2">
      <span className="relative flex items-center">
        <img src={avatarUrl} alt={fullName} className="w-8 h-8 rounded-full" />
        <span className="w-2 h-2 bg-green-800 rounded absolute top-8 left-5"></span>
      </span>
      <div>
        <h6>{fullName}</h6>
        <small>{title}</small>
      </div>
    </div>
  );
}

export default Status;
