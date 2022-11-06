import { useEffect } from 'react';

function Accordion({ options, title, isOpen = false }) {
  useEffect(() => {
    const checkClose = (e) => {
      const acc = document.getElementById('accordion');
      if (!acc.contains(e.target)) {
        acc.removeAttribute('open');
      }
    };
    document.addEventListener('click', checkClose);
    return () => {
      document.removeEventListener('click', checkClose);
    };
  });
  return (
    <details
      open={isOpen}
      className="cursor-pointer flex relative px-2"
      id="accordion"
    >
      <summary className="flex">{title}</summary>
      {options && (
        <ul className="absolute bg-white left-0 right-0 gap-4 p-3">
          {options.map((opt) => (
            <li key={opt}>{opt}</li>
          ))}
        </ul>
      )}
    </details>
  );
}

export default Accordion;
