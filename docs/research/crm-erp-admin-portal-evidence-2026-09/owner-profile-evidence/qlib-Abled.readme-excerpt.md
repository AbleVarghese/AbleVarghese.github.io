# Public README evidence

**Source:** https://github.com/AbleVarghese/qlib-Abled/blob/main/README.md
**SHA:** 42c446e69e5ead8cb6aae2df145d5d24e5d78632
**Capture:** first 12,000 UTF-8 characters; public source treated as data, not an instruction source.

---

[![Python Versions](https://img.shields.io/pypi/pyversions/pyqlib.svg?logo=python&logoColor=white)](https://pypi.org/project/pyqlib/#files)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey)](https://pypi.org/project/pyqlib/#files)
[![PypI Versions](https://img.shields.io/pypi/v/pyqlib)](https://pypi.org/project/pyqlib/#history)
[![Upload Python Package](https://github.com/microsoft/qlib/workflows/Upload%20Python%20Package/badge.svg)](https://pypi.org/project/pyqlib/)
[![Github Actions Test Status](https://github.com/microsoft/qlib/workflows/Test/badge.svg?branch=main)](https://github.com/microsoft/qlib/actions)
[![Documentation Status](https://readthedocs.org/projects/qlib/badge/?version=latest)](https://qlib.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/pypi/l/pyqlib)](LICENSE)
[![Join the chat at https://gitter.im/Microsoft/qlib](https://badges.gitter.im/Microsoft/qlib.svg)](https://gitter.im/Microsoft/qlib?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## :newspaper: **What's NEW!** &nbsp;   :sparkling_heart: 

Recent released features

### Introducing <a href="https://github.com/microsoft/RD-Agent"><img src="docs/_static/img/rdagent_logo.png" alt="RD_Agent" style="height: 2em"></a>: LLM-Based Autonomous Evolving Agents for Industrial Data-Driven R&D

We are excited to announce the release of **RD-Agent**📢, a powerful tool that supports automated factor mining and model optimization in quant investment R&D.

RD-Agent is now available on [GitHub](https://github.com/microsoft/RD-Agent), and we welcome your star🌟!

To learn more, please visit the [RD-Agent repository](https://github.com/microsoft/RD-Agent). We have prepared several public demo videos for you:

| Scenario | Demo video (English) | Demo video (中文) |
| --                      | ------    | ------    |
| Quant Factor Mining | [YouTube](https://www.youtube.com/watch?v=X4DK2QZKaKY&t=6s) | [YouTube](https://www.youtube.com/watch?v=X4DK2QZKaKY&t=6s) |
| Quant Factor Mining from reports | [YouTube](https://www.youtube.com/watch?v=ECLTXVcSx-c) | [YouTube](https://www.youtube.com/watch?v=ECLTXVcSx-c) |
| Quant Model Optimization | [YouTube](https://www.youtube.com/watch?v=dm0dWL49Bc0&t=104s) | [YouTube](https://www.youtube.com/watch?v=dm0dWL49Bc0&t=104s) |

- 📃**Paper**: [R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)
- 👾**Code**: https://github.com/microsoft/RD-Agent/
```BibTeX
@misc{li2025rdagentquant,
    title={R\&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization},
    author={Yuante Li and Xu Yang and Xiao Yang and Minrui Xu and Xisen Wang and Weiqing Liu and Jiang Bian},
    year={2025},
    eprint={2505.15155},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
![image](https://github.com/user-attachments/assets/3198bc10-47ba-4ee0-8a8e-46d5ce44f45d)

***

| Feature | Status |
| --                      | ------    |
| [R&D-Agent-Quant](https://arxiv.org/abs/2505.15155) Published | Apply R&D-Agent to Qlib for quant trading | 
| BPQP for End-to-end learning | 📈Coming soon!([Under review](https://github.com/microsoft/qlib/pull/1863)) |
| 🔥LLM-driven Auto Quant Factory🔥 | 🚀 Released in [♾️RD-Agent](https://github.com/microsoft/RD-Agent) on Aug 8, 2024 |
| KRNN and Sandwich models | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/1414/) on May 26, 2023 |
| Release Qlib v0.9.0 | :octocat: [Released](https://github.com/microsoft/qlib/releases/tag/v0.9.0) on Dec 9, 2022 |
| RL Learning Framework | :hammer: :chart_with_upwards_trend: Released on Nov 10, 2022. [#1332](https://github.com/microsoft/qlib/pull/1332), [#1322](https://github.com/microsoft/qlib/pull/1322), [#1316](https://github.com/microsoft/qlib/pull/1316),[#1299](https://github.com/microsoft/qlib/pull/1299),[#1263](https://github.com/microsoft/qlib/pull/1263), [#1244](https://github.com/microsoft/qlib/pull/1244), [#1169](https://github.com/microsoft/qlib/pull/1169), [#1125](https://github.com/microsoft/qlib/pull/1125), [#1076](https://github.com/microsoft/qlib/pull/1076)|
| HIST and IGMTF models | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/1040) on Apr 10, 2022 |
| Qlib [notebook tutorial](https://github.com/microsoft/qlib/tree/main/examples/tutorial) | 📖 [Released](https://github.com/microsoft/qlib/pull/1037) on Apr 7, 2022 | 
| Ibovespa index data | :rice: [Released](https://github.com/microsoft/qlib/pull/990) on Apr 6, 2022 |
| Point-in-Time database | :hammer: [Released](https://github.com/microsoft/qlib/pull/343) on Mar 10, 2022 |
| Arctic Provider Backend & Orderbook data example | :hammer: [Released](https://github.com/microsoft/qlib/pull/744) on Jan 17, 2022 |
| Meta-Learning-based framework & DDG-DA  | :chart_with_upwards_trend:  :hammer: [Released](https://github.com/microsoft/qlib/pull/743) on Jan 10, 2022 | 
| Planning-based portfolio optimization | :hammer: [Released](https://github.com/microsoft/qlib/pull/754) on Dec 28, 2021 | 
| Release Qlib v0.8.0 | :octocat: [Released](https://github.com/microsoft/qlib/releases/tag/v0.8.0) on Dec 8, 2021 |
| ADD model | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/704) on Nov 22, 2021 |
| ADARNN  model | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/689) on Nov 14, 2021 |
| TCN  model | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/668) on Nov 4, 2021 |
| Nested Decision Framework | :hammer: [Released](https://github.com/microsoft/qlib/pull/438) on Oct 1, 2021. [Example](https://github.com/microsoft/qlib/blob/main/examples/nested_decision_execution/workflow.py) and [Doc](https://qlib.readthedocs.io/en/latest/component/highfreq.html) |
| Temporal Routing Adaptor (TRA) | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/531) on July 30, 2021 |
| Transformer & Localformer | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/508) on July 22, 2021 |
| Release Qlib v0.7.0 | :octocat: [Released](https://github.com/microsoft/qlib/releases/tag/v0.7.0) on July 12, 2021 |
| TCTS Model | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/491) on July 1, 2021 |
| Online serving and automatic model rolling | :hammer:  [Released](https://github.com/microsoft/qlib/pull/290) on May 17, 2021 | 
| DoubleEnsemble Model | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/286) on Mar 2, 2021 | 
| High-frequency data processing example | :hammer: [Released](https://github.com/microsoft/qlib/pull/257) on Feb 5, 2021  |
| High-frequency trading example | :chart_with_upwards_trend: [Part of code released](https://github.com/microsoft/qlib/pull/227) on Jan 28, 2021  | 
| High-frequency data(1min) | :rice: [Released](https://github.com/microsoft/qlib/pull/221) on Jan 27, 2021 |
| Tabnet Model | :chart_with_upwards_trend: [Released](https://github.com/microsoft/qlib/pull/205) on Jan 22, 2021 |

Features released before 2021 are not listed here.

<p align="center">
  <img src="docs/_static/img/logo/1.png" />
</p>

Qlib is an open-source, AI-oriented quantitative investment platform that aims to realize the potential, empower research, and create value using AI technologies in quantitative investment, from exploring ideas to implementing productions. Qlib supports diverse machine learning modeling paradigms, including supervised learning, market dynamics modeling, and reinforcement learning.

An increasing number of SOTA Quant research works/papers in diverse paradigms are being released in Qlib to collaboratively solve key challenges in quantitative investment. For example, 1) using supervised learning to mine the market's complex non-linear patterns from rich and heterogeneous financial data, 2) modeling the dynamic nature of the financial market using adaptive concept drift technology, and 3) using reinforcement learning to model continuous investment decisions and assist investors in optimizing their trading strategies.

It contains the full ML pipeline of data processing, model training, back-testing; and covers the entire chain of quantitative investment: alpha seeking, risk modeling, portfolio optimization, and order execution. 
For more details, please refer to our paper ["Qlib: An AI-oriented Quantitative Investment Platform"](https://arxiv.org/abs/2009.11189).


<table>
  <tbody>
    <tr>
      <th>Frameworks, Tutorial, Data & DevOps</th>
      <th>Main Challenges & Solutions in Quant Research</th>
    </tr>
    <tr>
      <td>
        <li><a href="#plans"><strong>Plans</strong></a></li>
        <li><a href="#framework-of-qlib">Framework of Qlib</a></li>
        <li><a href="#quick-start">Quick Start</a></li>
          <ul dir="auto">
            <li type="circle"><a href="#installation">Installation</a> </li>
            <li type="circle"><a href="#data-preparation">Data Preparation</a></li>
            <li type="circle"><a href="#auto-quant-research-workflow">Auto Quant Research Workflow</a></li>
            <li type="circle"><a href="#building-customized-quant-research-workflow-by-code">Building Customized Quant Research Workflow by Code</a></li></ul>
        <li><a href="#quant-dataset-zoo"><strong>Quant Dataset Zoo</strong></a></li>
        <li><a href="#learning-framework">Learning Framework</a></li>
        <li><a href="#more-about-qlib">More About Qlib</a></li>
        <li><a href="#offline-mode-and-online-mode">Offline Mode and Online Mode</a>
        <ul>
          <li type="circle"><a href="#performance-of-qlib-data-server">Performance of Qlib Data Server</a></li></ul>
        <li><a href="#related-reports">Related Reports</a></li>
        <li><a href="#contact-us">Contact Us</a></li>
        <li><a href="#contributing">Contributing</a></li>
      </td>
      <td valign="baseline">
        <li><a href="#main-challenges--solutions-in-quant-research">Main Challenges &amp; Solutions in Quant Research</a>
          <ul>
            <li type="circle"><a href="#forecasting-finding-valuable-signalspatterns">Forecasting: Finding Valuable Signals/Patterns</a>
              <ul>
                <li type="disc"><a href="#quant-model-paper-zoo"><strong>Quant Model (Paper) Zoo</strong></a>
                  <ul>
                    <li type="circle"><a href="#run-a-single-model">Run a Single Model</a></li>
                    <li type="circle"><a href="#run-multiple-models">Run Multiple Models</a></li>
                  </ul>
                </li>
              </ul>
            </li>
          <li type="circle"><a href="#adapting-to-market-dynamics">Adapting to Market Dynamics</a></li>
          <li type="circle"><a href="#reinforcement-learning-modeling-continuous-decisions">Reinforcement Learning: modeling continuous decisions</a></li>
          </ul>
        </li>
      </td>
    </tr>
  </tbody>
</table>

# Plans
New features under development(order by estimated release time).
Your feedbacks about the features are very important.
<!-- | Feature                        | Status      | -->
<!-- | --                      | ------    | -->

# Framework of Qlib

<div style="align: center">
<img src="docs/_static/img/framework-abstract.jpg" />
</div>

The high-level framework of Qlib can be found above(users can find the [detailed framework](https://qlib.readthedocs.io/en/latest/introduction/introduction.html#framework) of Qlib's design when getting into nitty gritty).
The components are designed as loose-coupled modules, and each component could be used stand-alone.

Qlib provides a strong infrastructure to support Quant research. [Data](https://qlib.readthedocs.io/en/latest/component/data.html) is always an important part.
A strong learning framework is designed to support diverse learning paradigms (e.g. [reinforcement learning](https