import Prism from "prismjs/components/prism-core";
import "prismjs/components/prism-python";
import "prismjs/components/prism-rust";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-javascript";
import boilerplate from "./boilerplate";

const config = {
  api: {
    reconnect: {
      interval: 5000,
      attempts: 100,
    },
  },
  languages: {
    supported: ["python", "nodejs", "rust"],
    grammar: {
      python: Prism.languages["python"],
      nodejs: Prism.languages["javascript"],
      rust: Prism.languages["rust"],
    },
    boilerplate: {
      python: boilerplate.python,
      nodejs: boilerplate.nodejs,
      rust: boilerplate.rust,
    },
  },
};

export default config;
