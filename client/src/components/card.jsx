function Card({ title, icon, description, footer }) {
  return (
    <article className="flex flex-col justify-between bg-white p-8 text-center rounded-md shadow-lg">
      <div>
        <h3 className="text-2xl font-medium">{title}</h3>
        <i className="my-8 text-primary">{icon}</i>
        <p>{description}</p>
      </div>
      {footer && <p className="text-secondary font-semibold">{footer}</p>}
    </article>
  );
}

export default Card;
