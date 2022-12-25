---
title: A publishing infrastructure for AI-assisted academic authoring
keywords:
- manubot
- artificial intelligence
- scholarly publishing
- software
lang: en-US
date-meta: '2022-12-25'
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
  <meta name="dc.date" content="2022-12-25" />
  <meta name="citation_publication_date" content="2022-12-25" />
  <meta property="article:published_time" content="2022-12-25" />
  <meta name="dc.modified" content="2022-12-25T19:13:56+00:00" />
  <meta property="article:modified_time" content="2022-12-25T19:13:56+00:00" />
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
  <link rel="alternate" type="text/html" href="https://greenelab.github.io/manubot-gpt-manuscript/v/a087fc614168c6eec4e9dd6d71a403e537fb4cd2/" />
  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/manubot-gpt-manuscript/v/a087fc614168c6eec4e9dd6d71a403e537fb4cd2/" />
  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/manubot-gpt-manuscript/v/a087fc614168c6eec4e9dd6d71a403e537fb4cd2/manuscript.pdf" />
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
([permalink](https://greenelab.github.io/manubot-gpt-manuscript/v/a087fc614168c6eec4e9dd6d71a403e537fb4cd2/))
was automatically generated
from [greenelab/manubot-gpt-manuscript@a087fc6](https://github.com/greenelab/manubot-gpt-manuscript/tree/a087fc614168c6eec4e9dd6d71a403e537fb4cd2)
on December 25, 2022.
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


# Methods

We implemented the AI-based revision infrastructure in Manubot [@doi:10.1371/journal.pcbi.1007128].
Manubot takes Markdown as input and produces HTML, PDF, or other pandoc-supported formats as output.
It includes a robust cite-by-persistent-identifier infrastructure.
Its workflows are implemented in continuous integration software (Appveyor, GitHub Actions, etc).
Most workflows run with each commit.

We used the OpenAI API for access to large language models, with a focus on the completion endpoints.
This API incurs a cost with each run that depends on manuscript length.
Because of this cost, we implemented our workflow in GitHub actions, making it triggerable by the user.
The user can select the model that they wish to use, allowing costs to be tuned.
With the most complex model, `text-davinci-003`, the cost per run is under $0.50 for many manuscripts.

When the user triggers the action, the manuscript is parsed by section and then by paragraph, passed to the model along with a set of custom prompts, returned, reformatted, and output.
Our workflow then uses the GitHub API to generate a new pull request, allowing the user to review and, if desired, modify the output before merging.
This workflow allows text to be attributed either to the initial user or to the language model, which may be important in the event that future legal decisions alter the copyright landscape around the outputs of generative models.

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

