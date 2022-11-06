import { Link, useNavigate } from 'react-router-dom';
import cls from 'classnames';
import { useState } from 'react';

import Navbar from '../components/navbar';
import Button from '../components/button';

const steps = [
  { nb: 1, title: 'Submit', headline: 'submit' },
  { nb: 2, title: 'Review', headline: 'review' },
  { nb: 3, title: 'Refine', headline: 'refine' },
  { nb: 4, title: 'Funding', headline: 'funding' },
  { nb: 5, title: 'Decision', headline: 'decision' },
];

function ApplicationLayout({ children }) {
  const [step, setStep] = useState(1);
  const navigator = useNavigate();

  const selected = steps.find((st) => st.nb == step);

  function nextForm() {
    const next = Math.min(step + 1, steps.length);
    const nxt = steps.find((st) => st.nb == next);
    setStep(next);
    navigator(`#${nxt.headline}`);
  }

  return (
    <>
      <Navbar />
      <div className="flex">
        <aside className="w-3/12 flex flex-col">
          <div className="bg-gray-300 px-6 py-2 mb-6 text-center text-2xl font-medium">
            My application
          </div>
          <div>
            <ol className="flex flex-col gap-8 text-xl">
              {steps.map((st) => (
                <li
                  key={st.nb}
                  className={cls('mx-4 my-2', {
                    'font-semibold': step == st.nb,
                  })}
                >
                  <Link to={'#' + st.headline} onClick={() => setStep(st.nb)}>
                    <span className="p-2 w-4 h-4 mr-4 bg-secondary rounded-full font-semibold">
                      {st.nb}
                    </span>
                    {st.title}
                  </Link>
                </li>
              ))}
            </ol>
          </div>
        </aside>
        <div className="w-9/12 bg-gray-200 relative">
          {children}

          <div className="absolute flex gap-4 right bottom-0 right-0 bg-white">
            <Button className="w-24" shape="rounded" type="light">
              Back
            </Button>
            <Button className="w-24" shape="rounded" onClick={nextForm}>
              Next
            </Button>
          </div>
        </div>
      </div>
    </>
  );
}

export default ApplicationLayout;
