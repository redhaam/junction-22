function Select({ name, id, options }) {
  return (
    <select
      name={name}
      id={id}
      className="border border-gray-300 rounded-full text-gray-600 h-10 pl-5 pr-10 bg-white hover:border-gray-400 focus:outline-none appearance-none"
    >
      {options.map((opt) => (
        <option value={opt.value}>{opt.label}</option>
      ))}
    </select>
  );
}

export default Select;
