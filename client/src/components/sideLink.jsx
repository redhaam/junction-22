import { Link } from 'react-router-dom';
import cls from 'classnames';
function SideLink({ nb, headline, title, selected = false, onClick }) {
  return (
    <Link to={'#' + headline}>
      <div
        onClick={() => onClick && onClick(nb)}
        className={cls({
          'font-semibold': selected,
          'text-gray-700': !selected,
        })}
      >
        <span className="bg-secondary text-white h-5 w-5">{nb}</span>
        {title}
      </div>
    </Link>
  );
}

export default SideLink;
