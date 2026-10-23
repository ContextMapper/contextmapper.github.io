![Context Mapper](https://raw.githubusercontent.com/wiki/ContextMapper/context-mapper-dsl/logo/cm-logo-github-small.png)  
# contextmapper.org
[![Build & Deploy Website](https://github.com/ContextMapper/contextmapper.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/ContextMapper/contextmapper.github.io/actions/workflows/deploy.yml) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This is the repository of Context Mapper's website [https://contextmapper.org/](https://contextmapper.org/).

## Running Locally
To preview the website locally, follow these steps:

 1. Install Ruby (3.2 or newer) and the bundler in case you don't have it already:

 ```bash
 gem install bundler
 ```

 2. Install dependencies:

 ```bash
 bundle install
 ```

 3. Run the Context Mapper website (http://localhost:4000):

 ```bash
 bundle exec jekyll serve
 ```

## Writing Documentation
CML code blocks are highlighted by our own Rouge lexer ([`_plugins/cml_lexer.rb`](_plugins/cml_lexer.rb)); use `cml` as language:

````markdown
```cml
BoundedContext CustomerManagementContext implements CustomerManagementDomain {
  type = FEATURE
}
```
````

When the CML grammar gets new keywords, add them to the lexer as well.

## Deployment and Previews
 * **Production:** every push to `master` is built with Jekyll and deployed to [https://contextmapper.org/](https://contextmapper.org/) (GitHub Pages) by the [Build & Deploy Website](.github/workflows/deploy.yml) workflow. Pull requests are built (but not deployed) by the same workflow.
 * **Previews:** to review changes in the browser before merging them, run the [Deploy Preview (manual)](.github/workflows/preview.yml) workflow on your branch (_Actions_ > _Deploy Preview (manual)_ > _Run workflow_ > select the branch). The branch is deployed to Cloudflare Pages and the URL is shown in the workflow run summary (`https://<branch>.contextmapper-preview.pages.dev`). The previews are protected by Cloudflare Access; ask a maintainer to get access.

## Contribution
If you think something is missing on our documentation website and you still have unanswered questions, we are happy if you create an issue [here](https://github.com/ContextMapper/contextmapper.github.io/issues) allowing us to improve the docs. PRs are always welcome as well!

## License
This website is released under the [Apache License, Version 2.0](LICENSE). The fonts in `assets/fonts` ([Inter](https://github.com/rsms/inter) and [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)) are licensed under the [SIL Open Font License 1.1](assets/fonts).
