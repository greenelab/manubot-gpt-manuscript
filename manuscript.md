---
title: A publishing infrastructure for AI-assisted academic authoring
keywords:
- manubot
- artificial intelligence
- scholarly publishing
- software
lang: en-US
date-meta: '2023-01-10'
author-meta:
- Milton Pividori
- Casey S. Greene
header-includes: |
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta property="og:type" content="article" />
  <meta name="dc.title" content="A publishing infrastructure for AI-assisted academic authoring" />
  <meta name="citation_title" content="A publishing infrastructure for AI-assisted academic authoring" />
  <meta property="og:title" content="A publishing infrastructure for AI-assisted academic authoring" />
  <meta property="twitter:title" content="A publishing infrastructure for AI-assisted academic authoring" />
  <meta name="dc.date" content="2023-01-10" />
  <meta name="citation_publication_date" content="2023-01-10" />
  <meta property="article:published_time" content="2023-01-10" />
  <meta name="dc.modified" content="2023-01-10T21:01:19+00:00" />
  <meta property="article:modified_time" content="2023-01-10T21:01:19+00:00" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Milton Pividori" />
  <meta name="citation_author_institution" content="Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA" />
  <meta name="citation_author_orcid" content="0000-0002-3035-4403" />
  <meta name="twitter:creator" content="@miltondp" />
  <meta name="citation_author" content="Casey S. Greene" />
  <meta name="citation_author_institution" content="Center for Health AI, University of Colorado School of Medicine, Aurora, CO 80045, USA" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Colorado School of Medicine, Aurora, CO 80045, USA" />
  <meta name="citation_author_orcid" content="0000-0001-8713-9213" />
  <meta name="twitter:creator" content="@GreeneScientist" />
  <link rel="canonical" href="https://greenelab.github.io/manubot-gpt-manuscript/" />
  <meta property="og:url" content="https://greenelab.github.io/manubot-gpt-manuscript/" />
  <meta property="twitter:url" content="https://greenelab.github.io/manubot-gpt-manuscript/" />
  <meta name="citation_fulltext_html_url" content="https://greenelab.github.io/manubot-gpt-manuscript/" />
  <meta name="citation_pdf_url" content="https://greenelab.github.io/manubot-gpt-manuscript/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://greenelab.github.io/manubot-gpt-manuscript/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://greenelab.github.io/manubot-gpt-manuscript/v/46ec665965806fef3128ccfa26a0c117600db865/" />
  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/manubot-gpt-manuscript/v/46ec665965806fef3128ccfa26a0c117600db865/" />
  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/manubot-gpt-manuscript/v/46ec665965806fef3128ccfa26a0c117600db865/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://greenelab.github.io/manubot-gpt-manuscript/v/46ec665965806fef3128ccfa26a0c117600db865/))
was automatically generated
from [greenelab/manubot-gpt-manuscript@46ec665](https://github.com/greenelab/manubot-gpt-manuscript/tree/46ec665965806fef3128ccfa26a0c117600db865)
on January 10, 2023.
</em></small>



## Authors



+ **Milton Pividori**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-3035-4403](https://orcid.org/0000-0002-3035-4403)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [miltondp](https://github.com/miltondp)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [miltondp](https://twitter.com/miltondp)
    <br>
  <small>
     Department of Genetics, Perelman School of Medicine, University of Pennsylvania, Philadelphia, PA 19104, USA
  </small>

+ **Casey S. Greene**
  ^[✉](#correspondence)^<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-8713-9213](https://orcid.org/0000-0001-8713-9213)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [cgreene](https://github.com/cgreene)
    · ![Twitter icon](images/twitter.svg){.inline_icon width=16 height=16}
    [GreeneScientist](https://twitter.com/GreeneScientist)
    <br>
  <small>
     Center for Health AI, University of Colorado School of Medicine, Aurora, CO 80045, USA; Department of Biomedical Informatics, University of Colorado School of Medicine, Aurora, CO 80045, USA
  </small>


::: {#correspondence}
✉ — Correspondence possible via [GitHub Issues](https://github.com/greenelab/manubot-gpt-manuscript/issues)
or email to
Casey S. Greene \<casey.s.greene@cuanschutz.edu\>.


:::


## Abstract {.page_break_before}

Academics often communicate through scholarly manuscripts.
These manuscripts describe new advances, summarize existing literature, or argue for changes in the status quo.
Writing and revising manuscripts can be a time-consuming process.
Large language models are bringing new capabilities to many areas of knowledge work.
We integrated the use of large language models into the Manubot publishing ecosystem.
Users of Manubot can run a workflow, which will trigger a series of queries to OpenAI's language models, produce revisions, and create a timestamped set of suggested revisions.
Given the amount of time that researchers put into crafting prose, we expect this advance to radically transform the type of knowledge work that academics perform.


# Introduction

The manuscript pre-dates the invention of printing by thousands of years, but the practice of producing exclusively scientific journals only started roughly 350 years ago [@isbn:0810808447].
The implementation of external peer review varies by journal but for many is less than 100 years old [@doi:10/d26d8b].
To date, most manuscripts have been written by humans or teams of humans working together to describe scholarly advances.

Modern scholarly manuscripts often describe new advances, summarize existing literature, or argue for changes in the status quo.
However, writing and revising can be a time-consuming process.
Academics can sometimes be long-winded in getting to key points, making writing more impenetrable to their audience [@doi:10.1038/d41586-018-02404-4].

Modern computing capabilities and the widespread availability of text, images, and other data on the internet has laid the foundation for artificial intelligence (AI) models with many parameters.
Large language models, in particular, are opening the floodgates to new technologies with the capability to transform how society operates [@arxiv:2102.02503].
The GPT-3 model, with its 175 billion parameters, has demonstrated strong performance on many tasks [@arxiv:2005.14165].

We developed a software publishing platform that imagines a future where authors co-write their manuscripts with the support of large language models.
We used, as a base, the Manubot platform for scholarly publishing [@doi:10.1371/journal.pcbi.1007128].
Manubot was designed as an end-to-end publishing platform for scholarly writing for both individual and large-collaborative projects.
It has been used for collaborations of approximately 50 authors writing hundreds of pages of text reviewing progress during the COVID19 pandemic [@pmid:34545336].
We developed a new workflow that parses the manuscript, uses a large language model with section-specific custom prompts to revise the manuscript, and then creates a set of suggested changes to reach the revised state.
Changes are presented to the user through the GitHub interface for author review and integration into the published document.


# Implementing AI-based revision into the Manubot publishing ecosystem

## Overview

![
**AI-based revision applied on a Manubot-based manuscript.**
**a)** A manuscript (written with Manubot) with different sections.
**b)** Section-specific prompts used to process each paragraph.
If a paragraph belongs to a non-standard section, then a default prompt will be used to perform a basic revision only.
](images/figure_1.svg "AI-based revision applied on a Manubot manuscript"){#fig:ai_revision width="85%"}

We implemented the AI-based revision infrastructure in Manubot [@doi:10.1371/journal.pcbi.1007128].
Manubot is a tool for collaborative writing of scientific manuscripts.
It utilizes version control and a continuous integration workflow to facilitate efficient and transparent collaboration among authors.
Manubot integrates with popular version control platforms such as GitHub, allowing authors to easily track changes and collaborate on writing in real time.
Additionally, Manubot automates the process of generating a formatted manuscript (such as HTML, PDF, DOCX; Figure {@fig:ai_revision}a shows the HTML output), reducing the time and effort required for manuscript preparation and submission.
Built on this modern and open paradigm, our AI-based revision software was built using GitHub Actions, which allows the user to easily trigger an automated revision task on the entire manuscript or specific sections of it.


When the user triggers the action, the manuscript is parsed by section and then by paragraph (Figure {@fig:ai_revision}b), passed to the language model along with a set of custom prompts, returned, reformatted, and output.
Our workflow then uses the GitHub API to generate a new pull request, allowing the user to review and modify the output before merging the changes into the manuscript.
This workflow attributes text to either the human user or to the AI language model, which may be important if future legal decisions alter the copyright landscape around the outputs of generative models.


We used the [OpenAI API](https://openai.com/api/) for access to these models.
Since this API incurs a cost with each run that depends on manuscript length, we implemented an workflow in GitHub Actions that can be manually triggered by the user.
Our implementation allows users to tune the costs to their needs by allowing to select specific sections to be revised instead of the entire manuscript.
Additionally, several model parameters can be adjusted to tune costs even further, such as the language model version (including Davinci and Curie, and potentially newly published ones), how much risk the model will take, or the "quality" of the completions.
For instance, using Davinci models (the most complex and capable ones), the cost per run is under $0.50 for most manuscripts.


## Implementation details

Our tools are comprised of Python scripts that perform the AI-based revision ([https://github.com/greenelab/manubot-ai-editor](https://github.com/greenelab/manubot-ai-editor)) and a GitHub Actions workflow that integrates manuscript with Manubot.
The user only needs to run the workflow by specifing the branch that will be revised and selecting the files/sections of the manuscript (optional), the language model to use (`text-davinci-003` by default) and the output branch name.
As explained later, for more advanced users it is also possible change most of the tool's behavior or the language model parameters.


When the workflow is triggered, it downloads the manuscript by cloning the specified branch.
It revises all of the manuscript files, or only some of them if the user specifies a subset.
Next, each paragraph in the file is read and submitted to the OpenAI API for revision.
If the request is successful, the tool will write the revised paragraph in place of the original one using one sentence per line (which is the recommended format for the input text).
If the request fails, the tool might try again (up to five times by default) if it is a common error (such as "server overloaded") or a model specific error that requires to change some of its parameters.
If the error cannot be handled or the maximum number of retries is reached, the original paragraph is written instead with an HTML comment at the top explaining the cause of the error.
This allows the user to debug the problem and attempt to fix it if desired.


As shown in Figure {@fig:ai_revision}b, each API request comprises a prompt (the instructions given to the model) and the paragraph to be revised.
The prompt uses the manuscript title and keywords, so both have to be accurate for getting the best revision outcomes.
The other key component to process a paragraph is its section.
Some paragraphs are simpler to process than others.
For instance, the abstract is a set of sentences with no citations, whereas a paragraph from the Introduction section has several references to other scientific papers.
A paragraph in the Results section has fewer citations but many references to figures or tables, where enough details about the experiments must be provided to understand and interpret the outcomes.
The Methods section is more dependent on the type of paper, but in general it has to provide technical details and sometimes mathematical formulas and equations.
Therefore, we designed section-specific prompts, which we found led to the most useful suggestions.
Figures and tables captions, as well as paragraphs that contain only one or two sentences and less than sixty words, are not processed and copied directly to the output file.


The section of a paragraph is automatically inferred from the file name using a simple strategy (such as if "introduction" or "methods" is part of the file name).
If the tool fails to infer a section from the file, then the file will not be processed.
If this happens, the user is still able to specify which section the file belongs to.
The section could be a standard one (abstract, introduction, results, methods, or discussion) for which a specific prompt is used (Figure {@fig:ai_revision}b), or a non-standard one for which a default prompt will be used to instruct the model to perform only a basic revision (`minimize the use of jargon, ensure text grammar is correct spelling errors are fixed, and the text has a clear sentence structure`).
<!--
TODO:
  - make sure the documentation of the workflow mention this section mapping, and also custom sections (using the default prompt)
 -->


## Properties of language models

Our AI-based revision workflow uses [text completion](https://beta.openai.com/docs/guides/completion) to process each paragraph, either using the completion endpoint or the new edits endpoint (which is currently in beta).
We tested our tool using Davinci and Curie models, including `text-davinci-003`, `text-davinci-edit-001` and `text-curie-001`.
Davinci models are the most powerful GPT-3 model, whereas Curie ones are less capable but faster and less expensive.
Although the edits endpoints would be the ideal interface for our task, it is still in beta.
Therefore, we mainly focused on the completion endpoint.
<!-- REMEMBER TO SEND RESULTS TO OPENAI ABOUT THE edits endpoint, they are requesting feedback -->
All models can be fine-tuned using different parameters (see [OpenAI - API Reference](https://beta.openai.com/docs/api-reference/completions)), and the most important ones can be easily adjusted using our tool.


Language models for text completion have a context length that indicates the limit of tokens they can process (tokens are common character sequences in text).
This limit includes the size of the prompt and the paragraph, and the maximum number of tokens to generate for the completion (parameter `max_tokens`).
For instance, the context length of Davinci models is 4,000, and 2,048 for Curie (see [OpenAI - Models overview](https://beta.openai.com/docs/models/overview)).
For this reason, it is still not possible to use the entire manuscript as input, not even entire sections.
Therefore, our AI-assisted revision software process each paragraph of the manuscript with section-specific prompts, as shown in Figure {@fig:ai_revision}b.
The advantage of this approach is the ability to process large manuscripts by processing small chunks of text.
The main issue, however, is that the language model processes only a single paragraph from a section, potentially losing important context to produce a better output.
Nonetheless, we find that the model still produces high-quality output (see [Results](#sec:results)).
Additionally, since the goal of our tool is to revise a paragraph, by default we set the maximum number of tokens (parameter `max_tokens`) as twice the estimated number of tokens in the paragraph (one token approximately represents four characters, see [OpenAI - Tokenizer](https://beta.openai.com/tokenizer])).
The tool automatically adjusts this parameter and performs the request again if a related error is returned by the API.
The user can force the tool to either use a fixed value for `max_tokens` for all paragraphs, or change the fraction of maximum tokens based on the estimated paragraph size (two by default).


The language models used are stochastic: they will generate a different revision for the same input paragraph each time.
This behavior can be changed by using the "sampling temperature" or "nucleus sampling" parameters (we use `temperature=0.5` by default).
Although we selected default values that worked well across multiple manuscripts, these parameters can be changed by the user if necessary to make the model more deterministic.
The user can also instruct the model to generate, for each paragraph, several completions and select the one with the highest log probability per token, what can improve the quality of the revision.
Our proof-of-concept implementation generates only one completion (parameter `best_of=1`) to avoid potentially high costs for the user.
Additionally, our workflow allows to process either the entire manuscript or individual sections.
This allows to control costs more effectively while focusing on a single piece of text in which the user can run the tool several times and pick the prefered revised text.


# Results

We used this infrastructure to revise an existing manuscript as well as to author a new one.
We back-ported the changes in Manubot to a manuscript describing the Clustermatch Correlation Coefficient (CCC) [@doi:10.1101/2022.06.15.496326].
The CCC was designed to capture both linear and non-linear relationships between variables.
The CCC manuscript describes its use, in particular with gene expression data.

The abstract of the CCC manuscript before revision had a Flesh-Kincaid readability score of X and a grade level of Y.
> PREVIOUS_VERSION

After suggested revisions, the readability score was X and the grade level was Y and read as follows:
> NEW_VERSION

The full manuscript before AI-based revision is available at [link], and the revised version is available at [new_link].
We noticed that the model has difficulty with the Manubot citation style, which may lead to some references becoming incorrect.
This pipeline is not fully automated: authors will need to review changes and verify the output.

We also used this framework in the context of authoring a new manuscript that described a publishing infrastructure that implemented large language models to suggest revisions.
The abstract before revisions had a Flesh-Kincaid readability score of X and a grade level of Y and read as follows:
> Academics often communicate through scholarly manuscripts.
> These manuscripts describe new advances, summarize existing literature, or argue for changes in the status quo.
> Writing and revising manuscripts can be a time-consuming process.
> Large language models are bringing new capabilities to many areas of knowledge work.
> We integrated the use of large language models into the Manubot publishing ecosystem.
> Users of Manubot can run a workflow, which will trigger a series of queries to OpenAI's language models, produce revisions, and create a timestamped set of suggested revisions.
> Given the amount of time that researchers put into crafting prose, we expect this advance to radically transform the type of knowledge work that academics perform.

After suggested revisions, abstract had a Flesh-Kincaid readability score of X and a grade level of Y and read as follows:
> NEW_VERSION


# Conclusions

We implemented AI-based models into publishing infrastructure.
While most manuscripts have been written by humans, the process is time consuming and academic writing can be difficult to parse.
We sought to develop a technology that academics could use to make their writing more understandable without changing the fundamental meaning.
This work lays the foundation for a future where academic manuscripts are constructed by a process that incorporates both human and machine authors.

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
