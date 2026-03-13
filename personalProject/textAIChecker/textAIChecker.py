import re
import nltk
import numpy as np
from collections import Counter
from wordfreq import zipf_frequency
from math import log2

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

#######################################
# TOKENIZATION
#######################################

def tokenize_words(text):
    words = nltk.word_tokenize(text.lower())
    words = [w for w in words if re.match(r"[a-zA-Z']+", w)]
    return words

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)

#######################################
# METRICS
#######################################

def type_token_ratio(words):
    return len(set(words)) / len(words) if words else 0

def comma_ratio(text, total_words):
    return text.count(",") / total_words if total_words else 0

def rare_word_ratio(words, threshold=3):
    rare = sum(1 for w in words if zipf_frequency(w, 'en') < threshold)
    return rare / len(words) if words else 0

def avg_sentence_length(sentences):
    lengths = [len(tokenize_words(s)) for s in sentences]
    return np.mean(lengths) if lengths else 0

def sentence_variance(sentences):
    lengths = [len(tokenize_words(s)) for s in sentences]
    return np.var(lengths) if lengths else 0

def burstiness(sentences):
    lengths = [len(tokenize_words(s)) for s in sentences]
    if len(lengths) < 2:
        return 0
    mean = np.mean(lengths)
    std = np.std(lengths)
    return std / mean if mean else 0

def lexical_entropy(words):
    freq = Counter(words)
    total = len(words)

    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)

    return entropy

#######################################
# INTERPRETATION LAYER
#######################################

def interpret_ttr(ttr):
    if ttr < 0.4:
        return "Low vocabulary diversity"
    elif ttr < 0.6:
        return "Moderate vocabulary diversity"
    else:
        return "High vocabulary diversity"

def interpret_burstiness(b):
    if b < 0.15:
        return "Very uniform sentence length"
    elif b < 0.3:
        return "Moderate variation"
    else:
        return "High variation in sentence length"

def interpret_entropy(e):
    if e < 4:
        return "Low lexical randomness"
    elif e < 6:
        return "Moderate lexical variation"
    else:
        return "High lexical randomness"

def interpret_rare(r):
    if r < 0.02:
        return "Very common vocabulary"
    elif r < 0.06:
        return "Balanced vocabulary"
    else:
        return "Uncommon vocabulary usage"

#######################################
# MAIN ANALYSIS
#######################################

def analyze_text(text):

    words = tokenize_words(text)
    sentences = tokenize_sentences(text)

    metrics = {}

    metrics["total_words"] = len(words)
    metrics["sentences"] = len(sentences)

    metrics["type_token_ratio"] = type_token_ratio(words)
    metrics["rare_word_ratio"] = rare_word_ratio(words)
    metrics["comma_ratio"] = comma_ratio(text, len(words))
    metrics["avg_sentence_length"] = avg_sentence_length(sentences)
    metrics["sentence_variance"] = sentence_variance(sentences)
    metrics["burstiness"] = burstiness(sentences)
    metrics["lexical_entropy"] = lexical_entropy(words)

    ###################################
    # INTERPRETATION
    ###################################

    interpretation = {
        "TTR_meaning": interpret_ttr(metrics["type_token_ratio"]),
        "burstiness_meaning": interpret_burstiness(metrics["burstiness"]),
        "entropy_meaning": interpret_entropy(metrics["lexical_entropy"]),
        "rare_word_meaning": interpret_rare(metrics["rare_word_ratio"])
    }

    return metrics, interpretation


#######################################
# TEST
#######################################

if __name__ == "__main__":

    text = """
The Impact of Prompt Engineering on Code Correctness and Performance in AI-Assisted Programming 

John Andrew Balbarosa 

Andrei Collin Yapchulay 

Department of Computer Science 

Far Eastern University Institute of Technology 

Abstract 

Artificial Intelligence (AI) systems made for code generation greatly depend on one’s prompt engineering to create reliable and fast outputs. This paper highlights that the clarity, structure, and intent placed within prompts play a decisive role in knowing both code correctness and overall performance. Rather than treating AI as an entity capable of genuine reasoning or actual logical thinking, this study approaches it as a probabilistic “fill-in-the-blanks” mechanism that runs through pattern prediction. From this view, poorly formulated prompts are likely to introduce vagueness and reduce output quality, whereas carefully constructed prompts consistently lead to more accurate and reliable results. 

Keywords: Prompt Engineering, Code Generation, Artificial Intelligence, Large Language Models, Software Performance 

Shape 

Introduction 

Recent progress in large language models (LLMs) have made it possible for AI systems to help programmers in producing source code with increasing usefulness. Despite this recent growth, such systems do not have real cognitive understanding or thinking. Instead, they work by estimating the most statistically likely sequence of tokens based on patterns learned during the AI’s training. Because of this foundational procedure, the quality of the generated code is closely related to how precisely and thoughtfully the input prompt is created. 

1.1 Background of the Study 

This section investigates the theoretical foundations of Large Language Models (LLMs), regarding their probabilistic operation, the emergence of advanced capabilities as model scale increases, and the practical procedure through which prompt engineering shapes output generation. 

AI as a Probabilistic System 

At a fundamental level, AI-driven code generation can be understood as a structured prediction process, very similar when completing the missing elements within a given sequence. When shown with an incomplete input such as “The___is ___,” the model selects possible words according to probability distributions settled during training. Human judges then check whether the resulting output satisfies correctness standards, giving feedback that penalizes inaccurate outputs. This iterative process of adaptation, known as Reinforcement Learning from Human Feedback (RLHF), gradually improves model behavior. Thus, AI systems display adaptive statistical performance rather than genuine logical thinking or intentional reasoning. 

The Role of Model Scale and Parameter Density in Emergent Prompting Capabilities 

The research highlights a critical relationship between the number of parameters (model scale) and the emergence of specific capabilities. The paper posits that "emergence" occurs when a quantitative increase in the system (e.g., training compute or parameter count) results in a qualitative change in behavior.3 For many tasks, models operating with smaller embedding spaces—meaning fewer parameters and less training compute—demonstrate near-random performance (flat scaling curves) until a specific critical threshold is reached. Once this threshold is crossed, the expanded parameter density allows the model to suddenly "unlock" capabilities that were previously absent. 

Instruction Following (Task Construction) 

Instruction following stands out as one of the most visible emergent behaviors. In this setting, developers fine tune a model so it can perform new tasks by reading natural language instructions instead of relying only on example inputs. 

Impact of Parameters: Research shows that this method can harm performance in smaller models. Models with 7 = 1021  training FLOPs estimated around 8 billion parameters or fewer will often perform worse when developers finetune their commands/instructions. 3 

The Critical Threshold: Models start to transcribe and act on instructions effectively only after reaching a much larger scale. Once the parameter count grows into the hundreds of billions, instruction based task construction becomes dependable. A large parameter space make it possible for the model to generalize from instructions without becoming too confused. 

Chain-of-Thought Reasoning 

Chain of thought prompting helps a model to create a chain of middle reasoning steps before giving a final answer. This technique helps solve tasks that require multiple logical steps.4 

Impact of Parameters: Smaller models do not gain anything from this approach. When applied to models with lower parameter counts; fewer than billion parameters (FLOPs), chain of thought prompting often performs no better than standard prompting and can sometimes reduce the accuracy of the output itself. 3 

The Critical Threshold: Large models develop the ability to generate consistent intermediate reasoning steps. Models with hundreds of billions of parameters can maintain coherence across longer reasoning sequences, which makes chain of thought prompting effective. The effectiveness of generating these intermediate “thoughts” is an emergent ability that only appears in substantial models, such as LaMDA at 137B parameters or PaLM at 540B parameters. The added depth in parameters allows the model to maintain coherence across a longer sequence of logical steps. 

Program Execution and Algorithmic "Scratchpads" 

Another method uses what researchers call a “scratchpad.” Developers fine tune models to predict intermediate computational states while solving multi-step tasks such as complex arithmetic operations or code execution. 

Impact of Parameters: Unlike the massive scale required for general reasoning, this specific algorithmic ability emerges at a different scale. For tasks like 8-digit addition, the use of a scratchpad only becomes beneficial for models larger than ~ 40 million parameters (9 • 1019 FLOPs).3 

The Critical Threshold: Below this parameter count, the model cannot effectively utilize the intermediate "scratchpad" space to track its computation. However, once the threshold is crossed, performance jumps to nearly 100% accuracy, illustrating a sharp phase transition in the model's ability to manipulate symbolic data. 

 

Grounded Conceptual Mappings and Calibration 

This category touches upon the "embedding space" aspect—how models map language to conceptual or spatial domains, and how they understand their own knowledge (calibration). 

Grounded Mappings: In tasks requiring the mapping of conceptual domains (e.g., spatial directions in a grid world), performance remains near-random for almost all model sizes until the very largest GPT-3 scale is reached. This implies that a massive parameter space is necessary to internally represent and navigate these abstract conceptual "worlds".3 

Calibration: This refers to a model's ability to predict whether it can answer a question correctly. The "True/False" calibration technique (evaluating the probability that a proposed answer is true) only becomes superior to standard methods when the model scales to approximately 52 billion parameters (3 • 1023 FLOPs). 

Theoretical Frameworks in Prompt Retrieval 

Research suggests the use of AI in historical prompt retrieval to add to its next response, potentially utilizing principles similar to Bayesian inference for in-context learning , . This allows models to update their internal beliefs based on the "evidence" provided in the prompt history, approximating an implicit Bayesian update to select the most likely task or concept. 

Psychometric Properties and Representational Capacity 

Recent research demonstrates that a model's capacity for attention and size are critical determinants of its ability to maintain and express complex social traits. Studies that evaluate the shaping of synthetic personality show that larger models perform much better when handling complex or unclear instructions, especially when they must manage several personality dimensions at the same time. Smaller models can imitate individual traits, but they often struggle with what researchers describe as representational capacity. This limitation leads to narrower scoring ranges and weaker control once prompts become more complex or contain multiple layers. 

  

Larger models such as Flan PaLM 540B and GPT-4o rely on stronger in-context learning to process different pieces of social information more effectively. This allows them to maintain a consistent assigned persona with higher accuracy and better precision across downstream tasks. 

Effect of Prompt Engineering on Code Correctness 

Prompt engineering refers to the practice of crafting inputs that clearly specify intent, constraints, and expected outputs. Hyperspecific and well-structured prompts resemble the mental models of experienced programmers, allowing the AI to generate more accurate and maintainable code. A study by Marvin et al. (2023) establishes a comprehensive framework for prompt engineering by categorizing strategies like zero-shot and few-shot learning to standardize AI performance. Their research addresses the inconsistency of model outputs by treating prompt design as a structured lifecycle of refinement rather than just a simple instruction. Ultimately, the paper provides a roadmap for "Prompt Construction," demonstrating how systematic templates can effectively guide an LLM’s internal parameters to produce reliable results. 

Zero-Shot Prompt: "Translate the following English text to French: 'The quick brown fox jumps over the lazy dog.'" 

Few-Shot Prompt: "Translate the following English text to French: 'Apple' -> 'Pomme', 'Banana' -> 'Banane', 'The quick brown fox jumps over the lazy dog' -> " 
This study highlights that providing these "shots" (examples) standardizes the output format for the LLM. 

Logic and Template Dependence 

Additionally, research conducted by Wang et al. (2023) proves that AI does not fully require our logic to be impeccable. By testing models with completely invalid reasoning steps, they found out that the AI can still achieve 80-90% of its normal success rate despite it . Their paper proves that AI makes use of prompts given to them as structural templates to activate pre-trained knowledge; it does not learn to reason from specific examples. 

Original Prompt Sample (Valid CoT): "Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total? Rationale: Originally, Leah had 32 chocolates and her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 – 35 = 39 pieces left in total. The answer is 39." 

Invalid CoT Reasoning: "Originally, Leah had 32 chocolates and her sister had 42. So her sister had 42 – 32 = 10 chocolates more than Leah has. After eating 35, since 10 + 35 = 40, they had 45 – 6 = 39 pieces left in total. The answer is 39." 
This study proves that even with the "Invalid" math above, the AI still solves its own new problems correctly because it follows the step-by-step format. 

Contextual Infilling 

Furthermore, a study by Donahue et al. (2020) introduces the "Infilling by Language Modeling" (ILM) framework, which trains AI to predict missing spans of text by rearranging data so the model considers both preceding and subsequent context . In other words, they are trained to predict the next word in a sequence; the AI is made to look at a sentence with a hole in the middle and figure out exactly what fits there based on both what came before and what comes after. 

Infilling Prompt: "Lily always loved to read. She wondered sometimes, what it would be like to write a book? [blank] Lily did well in the course, and during it, wrote a short book." 

ILM Output: " She decided to take a course on fiction writing. " 

Comparative Prompt Analysis 

Poor Prompt Example: "Write a sorting program." This vague instruction often results in incomplete code, missing edge case handling, or inefficient algorithms. 

Improved Prompt Example: "Create a C++ program that uses Merge Sort for an integer array of size n, includes time complexity analysis, and handles duplicate values." This prompt constrains the problem space, making it led to a more correct and optimized code output. 

 

Review of Related Literature  

 

The field of Natural Language Processing (NLP) has changed dramatically over the last decade, moving from task-specific, handcrafted architectures to large, general-purpose language models. This shift is driven by three main factors: rapid growth in model parameters and training compute, improved alignment techniques such as Reinforcement Learning from Human Feedback (RLHF), and the development of prompting strategies that bring out hidden reasoning abilities. As models have become more complex, the need for careful evaluation has grown. Researchers now use multidimensional benchmarks that measure reasoning, safety, personality, and domain expertise, moving beyond simple linguistic metrics. This report reviews both foundational and recent literature to describe the current state of large language models. By combining insights from studies on emergent abilities, instruction tuning, chain-of-thought reasoning, and psychometric testing, it creates a structured overview of the technological landscape. The analysis examines how increases in model scale lead to qualitative improvements in performance, tests how alignment methods reduce hallucinations, and looks at patterns in how current reasoning processes are structured. The report also addresses the growing area of LLM psychometrics and the need for benchmarks that are dynamic and resistant to contamination. This chapter goes into detail on specific research areas, carefully checking references against the original sources. For each subsection, it identifies key figures, page numbers, and statistical thresholds, and combines them into a coherent account of how LLM capabilities have evolved. 

Detailed Literature Verification and Analysis 

 

 Emergent Abilities of Large Language Models (Wei et al.) 

A. Detailed Literature Verification and Analysis 

Emergent Abilities of Large Language Models (Wei et al.): 

Emergence in large language models refers to capabilities that smaller models do not show but appear when the model grows past a certain size. Wei et al. (2022) describe this phenomenon and show that these abilities appear suddenly after a critical scale, rather than gradually. This goes against the usual expectation from scaling laws, which assume that performance improves steadily as compute and parameter counts increase. 

Defining Emergence and Phase Transitions 

Wei et al. compare emergence to a phase change in physical systems. In those systems, small changes like temperature can trigger clear state changes, such as water freezing. In large language models, adding more training FLOPs or increasing the parameter count can create similar jumps in behavior. Abilities that do not appear in smaller models can suddenly appear in larger ones once the system reaches enough scale. The authors consider a capability emergent if smaller models do not display it but larger models do. Performance data supports this: models perform near-randomly across much of the scaling curve, and only after reaching a critical mass do their abilities improve sharply. 

Visualizing the Paradigm Shift 

The paper illustrates the standard prompting paradigm in Figure 1 on Page 3, titled “Example of an input and output for few-shot prompting.” 

 

 

Figure 1 

The diagram shows an input sequence with sentiment analysis examples, such as “Review: This movie sucks. Sentiment: negative,” followed by a target example, “Review: love this movie Sentiment:,” which the model completes with “positive.” The figure highlights the move from fine-tuning to in-context learning, where the model’s parameters stay fixed and the task is defined entirely by the prompt. 

 

 

 

Empirical Evidence of Emergence 

Figure 2 on Page 3 aggregates eight distinct emergent abilities across five model families, providing clear empirical evidence: 

 

 

 

Figure 2 

• Arithmetic Reasoning: Sub-figures 2A–2D show tasks from the BIG-Bench suite. GPT-3’s performance on 3-digit addition and subtraction, and 2-digit multiplication, stays near zero until around 2·10²² training FLOPs (roughly 13 billion parameters), where it jumps sharply above random chance. LaMDA shows a similar jump at 10²³ FLOPs (about 68 billion parameters). Differences between model families suggest that architecture and training data quality influence when emergence occurs. 
 
• Truthfulness: Figure 2E presents results from the TruthfulQA benchmark. Smaller Gopher models fail to exceed random performance. Only when the model scales to 5·10²³ FLOPs (around 280 billion parameters) does performance rise significantly, exceeding random chance by over 20%. This indicates that distinguishing truth from common misconceptions requires very large capacity. 
 
• Multi-task Understanding: Figure 2G shows results on the Massive Multi-task Language Understanding (MMLU) benchmark. Models with around 10²² FLOPs (10 billion parameters) do not outperform random guessing across the 57 MMLU topics. Emergence becomes substantial only at 3–5·10²³ FLOPs (70B–280B parameters). 

 

 

Alternative Metrics for Scale  

Wei et al. (2022) also look at other ways to measure it while parameter count and FLOPs are the usual measures of model scale. Figure 4 on Page 2 shows emergent abilities plotted against WikiText103 perplexity.  

 

Figure 3 

This approach is important because it connects the language modeling goal—predicting the next token—with actual downstream performance. The text notes that WikiText103 perplexity aligns closely with the amount of training computation for models such as Gopher and Chinchilla. Figures 10, 11, and 12 in Appendix D (also referenced on Page 2) provide additional scaling curves using parameter counts on the x-axis, which supports the emergence patterns observed in the main analysis. 

 

Figure 4 

 

Figure 5 

 

 

Figure 6 

Implications for Scaling Laws  

The results make the story of scaling laws less simple. Cross-entropy loss generally improves steadily across more than seven orders of magnitude, but task performance does not follow the same pattern. This shows that reducing loss and improving abilities are not directly linked. Phase transitions mean we cannot reliably guess what a 1-trillion or 10-trillion parameter model can do based only on a 100-billion parameter model. 
 
Comparing Chinchilla and Gopher adds more clarity. Chinchilla uses a similar amount of compute but only one-fourth of Gopher’s parameters. This suggests that the balance between data and parameters matters. Scaling parameters alone does not guarantee that new abilities will emerge; data-optimal scaling plays a key role in driving these capabilities. 

 

Training Language Models to Follow Instructions with Human Feedback (Ouyang et al.) 

While scaling gives a model the raw capacity for intelligence, it does not ensure that the model will follow user intent. The paper Training Language Models to Follow Instructions with Human Feedback (Ouyang et al., 2022) introduces InstructGPT, a model that shifted attention from just size to alignment. The work shows that Reinforcement Learning from Human Feedback (RLHF) can improve efficiency, allowing smaller models to perform better than larger models that are not aligned. 
 
The Alignment Methodology  
The main contribution of this study is the RLHF process, shown in Figure 2 on Page 2 of the source. The diagram presents a three-stage pipeline that aligns the model with human intentions for truthfulness, helpfulness, and harmlessness. 

 

Figure 7 

The diagram depicts a three-stage pipeline designed to align the model with the implicit intentions of truthfulness, helpfulness, and harmlessness: 

Supervised Fine-Tuning (SFT): The first stage collects demonstrations from human labelers. Contractors provide the desired output for each prompt, and these examples are used to fine-tune a GPT-3 baseline through supervised learning. 

Reward Model (RM) Training: Next, the model produces several outputs for a single prompt. Human labelers rank these outputs from best to worst. The dataset from human rankings is used to teach the Reward Model which outputs people like more. 

Reinforcement Learning (PPO): In the final stage, the SFT model goes through another round of training using Proximal Policy Optimization. The model creates outputs, and the Reward Model ranks them. PPO then uses these rankings to guide the model, nudging it toward producing better responses. 

Quantifying the Alignment Dividend  

The results from this approach are striking. Figure 1 on Page 2 shows a “Win rate” chart comparing several models against a 175B SFT baseline. 

 

Figure 8 

The y-axis shows the win rate, and the x-axis lists model sizes (1.3B, 6B, 175B). A key observation is that outputs from the 1.3 billion parameter InstructGPT model (PPO-ptx) were preferred by human evaluators over outputs from the much larger 175 billion parameter GPT-3. This suggests that alignment techniques can provide a huge efficiency gain: a smaller, aligned model can perform better than a massive, unaligned one on user-facing tasks. 
 
Improvements in Truthfulness and Hallucination 
The paper also reports concrete statistics on reliability. The authors define “truthfulness” as avoiding made-up information. 
 
 

Hallucination Rates: On closed-domain tasks, where the model relies only on the input, InstructGPT hallucinated less often than GPT-3. Specifically, the paper notes a 21% hallucination rate for InstructGPT versus 41% for GPT-3. Cutting hallucinations by roughly half is a major improvement in grounding. 

TruthfulQA: On the TruthfulQA benchmark, InstructGPT provides truthful and informative answers about twice as often as GPT-3. The authors note that this happens by default, meaning the model shows improved honesty without special prompting. 

Adversarial Robustness: These results hold even for subsets of questions that were not adversarially chosen, although the improvement is slightly smaller in those cases. 
 
 

 
 

Human Data Collection  

The quality of human feedback plays a critical role. The paper reports that 40 contractors labeled the data. They were chosen through a screening test to ensure high agreement rates and a shared understanding of the alignment goals: helpfulness, honesty, and harmlessness. Evaluations include 95% confidence intervals for error bars, supporting the statistical significance of the observed preference wins. 
 
 

Analysis of Implications 

The InstructGPT paper signals the move from the “scaling era” to the “alignment era.” It shows that the standard language modeling objective—predicting the next token—is not enough for building a helpful assistant. By adding human preferences directly into the optimization loop through RLHF, developers can direct the model’s raw power toward useful behavior. Still, a 21% hallucination rate remains. This dictates that RLHF is effective, however, is not a complete solution. The model learns to act helpful and honest as judged by humans, but it does not gain a fully strong internal understanding of truth. 

 

Towards Understanding Chain-of-Thought Prompting (Wang et al.) 

Chain-of-Thought (CoT) prompting became a widely used method for bringing forth reasoning behavior from large language models. The paper “Towards Understanding Chain-of-Thought Prompting: An Empirical Study of What Matters” (Wang et al., 2023) tells the reason why this technique works very well. Its findings challenge the common belief that models actually reason in the same way humans do. 

 

Deconstructing the Reasoning Process  

Figure 1 on Page 1 shows the core experimental setup. 

 

 

Figure 9 

The authors compare three prompting conditions: Standard Prompting, CoT Prompting, and an ablation condition called “Invalid Reasoning.” They use an arithmetic word problem about Leah and chocolates as the example. 

Valid Logic: In the standard CoT rationale, the reasoning is very clear. Leah starts with 32 chocolates, her sister has 42, giving a total of 74. After they eat 35, the remaining amount becomes 39. 

Invalid Logic: On the other hand, the invalid rationale contains incorrect and illogical steps. It mixes unrelated operations and produces nonsensical intermediate results, yet it still ends with the correct final answer of 39. 

The most astonishing result appeared in the performance bars in Figure 1. Even when the prompt includes flawed reasoning steps, models still reach over 80 to 90 percent of the performance achieved with valid CoT examples. Despite the logical errors in the demonstrations, the model continues to generate coherent reasoning during inference. This suggests that the prompt does not teach reasoning itself. Instead, it activates a capability that already exists within the model. 

 

Figure 10 

Structural Components of Rationale  

To explain this behavior, the authors break a rationale into two main parts, summarized in Table 1 on Page 2. 

First are bridging objects. These include the key semantic or numerical elements needed to reach a solution. In arithmetic tasks, they appear as numbers and equations. They appear as important entities or facts in factual question answering. 

Second are language templates. These consist of the connective phrases, relations, and structural cues that guide the model from one step to the next. 

Critical Success Factors 

The study finds that logical correctness in the example steps contributes only a small portion of the overall performance gain. Two other factors matter much more: 

Relevance to the Query: Relevance to the query plays a major role. The rationale must mention the correct entities and topics. Proper ordering also matters. The reasoning must follow a clear step-by-step sequence. 

Correct Ordering:  

Together, these results point to a form of structural mimicry. The model recognizes the pattern of a step-by-step explanation and the expected depth of computation. It then applies its own internal logic to solve the new problem, even when the example reasoning contains errors. 
 
 

Implications for Prompt Engineering 

These findings change how developers should approach prompt design. Instead of focusing on perfectly written logical explanations, it becomes more effective to provide examples that establish the correct structure and topic relevance. The prompt works like a formatting guide instead of a detailed tutorial. 
 
This supports the idea that large language models already develop dormant reasoning abilities during pre-training. A well-structured prompt does not teach them how to reason. It simply signals that a multi-step response is expected and activates the behavior accordingly. 

Enabling Language Models to Fill in the Blanks (Donahue et al.) 

Before the dominance of decoder-only models for all tasks, the paper "Enabling Language Models to Fill in the Blanks" (Donahue et al., 2020) proposed a novel framework to extend the capabilities of autoregressive models. This work, detailed in source 2005.05339v2.pdf , introduces the Infilling by Language Modeling (ILM) framework. 
 

 

Figure 11 

The ILM Framework The mechanism of ILM is visualized in Figure 1 on Page 1 of the paper. The diagram illustrates the transformation of a standard text generation task into an infilling task. 

Task Definition: The system takes incomplete text with blanks (e.g., "She ate [blank] for [blank]") and outputs the completed text ("She ate leftover pasta for lunch"). 

Training Methodology: The method builds each training example by combining the masked version of the text, denoted as x-tilde, with the spans that were removed, labeled as y. A special [sep] token marks where the visible context ends and the missing content begins, while [answer] tokens separate the individual spans that must be recovered. With this structure, a left-to-right model such as GPT-2 can first read the available context, then generate the missing segments step by step in sequence. 

 

Figure 12 

Construction Details 

Figure 2 on Page 2 illustrates a full example of how the training samples are formed. One of the most notable aspects of the method is how little extra length it introduces. Each sequence adds only 2k + 1 tokens beyond the original text, with k representing the number of removed spans. In the reported experiments, this value averaged roughly two spans per sample. Because the increase remains small, the model can learn infilling behavior without placing a heavy additional load on training computation. 

Performance and Human Evaluation 

The researchers evaluated the framework in three domains: short stories, scientific abstracts, and song lyrics. Human assessment produced particularly strong results in the short story setting. Evaluators frequently struggled to tell whether inserted sentences came from the model or a human writer. This outcome indicates that the system preserved contextual continuity and narrative flow well enough to produce coherent additions, something that earlier work often associated with bidirectional models. 

Implications for Architecture 

This framework also foreshadows what later became known as Fill In The Middle training objectives, which are now widely used in code generation systems. By reformulating a non sequential problem into a left to right generation process, the authors demonstrated how flexible decoder only models can be. The result supports a broader trend in later research: with carefully designed input formatting, autoregressive architectures can handle tasks once thought to require specialized structural designs. 

 

Conversational User-AI Intervention (Sarkar et al.) 

As large language models move into real user environments, mismatches between user intent and model interpretation have become a major source of failure. Sarkar et al. (2025) has examined this issue and proposed an automated intervention system designed to repair unclear prompts during an ongoing conversation. 

 

 

 

 

 

Figure 13 

The Intervention Framework  

Figure 1 on Page 3 shows the workflow of the intervention process. 

 

The figure depicts a retroactive intervention workflow: 

Detection: For the detection, the system first monitors conversation history for signals of dissatisfaction. These signals usually show up as short corrections from the user. In one example, the user said, “Nope! I wanted a multiplayer game.” It was clear the model had misunderstood the request. 

Rewrite Candidate Selection: Once dissatisfaction is detected, the system goes back through the conversation to find the message that caused the problem. Here, it singles out the brief query “Ruleta Casino,” which didn’t give enough information for the model to understand what the user really wanted. 
 
 

Rewriting: A specialized rewriting model reworks this vague input into a more clear, explicit version. The rewritten prompt expresses the user’s intended meaning more clearly and helps the main model make a response that fits the request. 

 

Key Findings  

The study evaluated this intervention strategy over five different language models, and that includes both open and proprietary systems. Results show that rewritten prompts consistently produced higher quality responses than the original inputs. The authors also observed that the benefit grows as conversations become longer, since additional dialogue context helps the rewriting model infer the user’s intent more accurately. 

 

Model Efficiency  

Another practical outcome concerns deployment strategy. The experiments demonstrate that relatively small models can serve effectively as rewriting agents for much larger generation models. This arrangement supports a mixture of roles which is a lightweight system interprets and clarifies user intent, while a more powerful model focuses on producing the final response. Separating these functions improves overall performance without requiring proportional increases in computational resources. 

Personality Traits in Large Language Models (Serapio-Garcia et al.) 

The paper Personality Traits in Large Language Models (SerapioGarcia et al., 2025) goes beyond basic functional abilities to study how synthetic personas behave. By using strict psychometric testing, the authors ensure that LLMs act in consistent and predictable ways, which is crucial for safe and reliable deployment. 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Psychometric Validation Methodology  

 

 

Figure 14 

The study uses a structured five-step method, shown in Figure 1 on Page 3, called the “Process for Establishing Construct Validity.” 

 

 The authors established a five-step pipeline: 

Administration: The models take widely used personality tests, including IPIP-NEO and BFI. 

Reliability Evaluation: Tools such as Cronbach’s Alpha, Guttman’s Lambda 6, and McDonald’s Omega will be used to measured the the consistency of the model’s responses. 

Convergent/Discriminant Validity: Model traits are evaluated against external benchmarks, including indicators like aggression or creativity. 

Criterion Validity: Checking alignment with external criteria (e.g., aggression, creativity). 

Construct Validity Judgment: A final yes/no decision determines whether each trait is reliably represented. 
 
 

Rigorous Statistical Thresholds 

Unlike earlier anecdotal studies, the authors enforce clear numerical thresholds. For a trait to be validly simulated: 

Reliability scores must be 0.70 or higher. 

Convergent correlations should reach 0.80 or above. 

Discriminant correlations need to differ by at least 0.40 on average. 

Scale and Shaping  

The researchers evaluated 18 different LLMs, generating over 1,200 responses per model with varied biographical prompts to produce statistically sound results. They also showed that personality traits could be finely adjusted, controlling them across nine levels using 104 specific descriptive adjectives. 

 

Implications for Safety  

 

The key finding that larger, instruction-tuned models show stronger reliability and validity indicates that personality in LLMs emerges as a stable property of semantic coherence rather than as random noise. Stability is critical for safety. If a model’s personality, such as its tendency toward agreeableness or rule-following, changes unpredictably, it cannot be deployed reliably. Controlling these traits lets developers design models with specific behavioral profiles. For instance, a model could act as a conscientious medical assistant or as an outgoing creative writing partner, with confidence that its behavior will remain consistent. 
 
Finally, the book chapter Prompt Engineering in Large Language Models (Marvin et al., 2024) offers a practical framework for applying the theoretical insights discussed above. 

 

 A Survey on Large Language Model Benchmarks (Ni et al.): 

 

A Survey on Large Language Model Benchmarks (Ni et al.): As LLM capabilities have grown rapidly, evaluation methods have become scattered and hard to compare. The survey “A Survey on Large Language Model Benchmarks” (Ni et al., 2025) tries to bring order to this situation by organizing the existing landscape. 
 
The Taxonomy of Evaluation 

The survey examines 283 representative benchmarks and groups them into three main tiers: 
 
1.) General Capabilities: Measuring core language ability, knowledge, and reasoning (e.g., MMLU, GLUE). 
 
2.) Domain-Specific: Targeting specialized areas such as natural sciences, law, and engineering (e.g., BioLLMBench, LawBench). 
 
3.) Target-Specific: These benchmarks concentrate on risks, reliability, and agent‑like behavior (e.g., SafetyBench, AgentBench). 

 

 
  

 

 

 
Visualizing the Timeline  

 

Figure 15 

Figure 1 on Page 1 presents a “Timeline of representative LLM benchmarks,” showing how evaluation trends changed between 2018 and 2025. The pattern over time is fairly clear: 
 
• 2018–2019: Work centered mostly on linguistic understanding tasks (GLUE, SQuAD). 
• 2020–2021: Attention shifted toward multi‑task knowledge evaluation (MMLU) and robustness. 
• 2024–2025: There was a sharp rise in benchmarks focused on agents and safety concerns (LiveBench, MMLU‑Pro, SafetyBench). 
 
Critical Failures of Current Benchmarks  

The survey identifies two systemic weaknesses in today’s evaluation ecosystem: 
 
Data Leakage: Because models train on massive internet-scale datasets, they sometimes memorize portions of static benchmark test sets. This can push benchmark scores higher than they should be, since strong results may come from memorizing test data rather than showing real generalization. 
 
Static Evaluation: Fixed datasets also have trouble reflecting real LLM usage. In practice, interactions tend to unfold across multiple turns, with context changing and user goals shifting over time. Simple metrics like Accuracy or BLEU do not capture these aspects well, and they miss whether a model’s reasoning process is reliable or safe. 
 
Future Directions 

 The survey points to what the authors describe as dynamic benchmarking. Here, evaluation tasks are not fixed—they can change over time or be generated automatically. This makes it harder for models to rely on memorized test data. The paper also stresses the importance of process evaluation, which means judging more than just the final output. It involves checking whether the reasoning steps used to reach an answer are valid and logically consistent. 
 
 

 Prompt Engineering in Large Language Models (Marvin et al.): 

 
The section discusses the application of the preceding concepts. It provides the evidence that prompt design is not simply black magic but a structurized process, and coherent and clear prompts can direct the model to generate better responses. 

The Prompting Framework The chapter describes prompt engineering as a system with clear parts. Table 1 (Pages 4–5) lists the main components: Instruction, Input Data, Context, and Output Indicator. Treating prompts this way makes them easier to design and adjust. The authors also note that having a clear structure—especially providing context and specifying the desired output format—often has a stronger impact than the exact wording of the logical content itself. This point is consistent with the findings reported by Wang et al. (2023). 

 

The Five‑Step Process Section 2.1 presents, in simple terms, a streamlined process of creating prompts that work well: 
 
1.) Specify the Task: Articulate what it is that you expect the model to give you. 
 
2.) Model Capabilities: Get to know what the model can do and understand its capacities. This includes any type of input it handles, their modalities and where the limitations lie. 
 
3.) Select Format: Pick the kind of result or output you want to get, like JSON or an essay or a list. 
 
4.) Add Context: Add in contextual information to guide the model interpretation. 
 
5.) Test and Refine: Take a look at the results and iterate on the prompt by making certain tuning adjustments to it. 

 

Analysis of Implications 

The framework supports linking research with the real world. When prompts are perceived as code units, developers can follow standard practices of software development: to test, version control and iteratively refine. This structured approach helps make LLM-based systems more consistent and dependable, especially when building real-world applications on top of probabilistic models. 

 

Evaluating Large Language Models Trained on Code (Chen et al.) 

Code generation provides a clear way to evaluate LLM performance because correctness is easy to verify: the code either runs successfully, or it does not. The paper “Evaluating Large Language Models Trained on Code” (Chen et al., 2021) introduced Codex, a GPT-based model fine-tuned on GitHub code, along with the HumanEval benchmark. 

 

Key Statistics and Findings 

The Power of Domain Specificity: The results show a large gap between general and specialized models. On the HumanEval benchmark, GPT-3 in a zero-shot setting solved none of the problems, while the fine-tuned Codex model solved 28.8%. This demonstrates how domain-specific training can turn a capability from absent into usable. 

Sampling as a Strategy: The study also shows that LLMs behave like probabilistic search systems, not simple knowledge lookups. When Codex was allowed to generate many possible answers—up to 100 per problem—its success rate climbed from 28.8% to 70.2%. This suggests the model often has the right solution somewhere in its range of outputs, even if it does not appear on the first try. Looking at multiple samples simply makes it easier to find it. 

 potential solutions. 

Metric Innovation: The authors argued that text-matching metrics such as BLEU do not work well for code evaluation. Instead, they proposed functional correctness—measuring whether generated code passes unit tests—as the most reliable standard. 

 

 

Implications 

This line of research formalized the “pass@k” metric, which later became a standard benchmark for evaluating code generation systems. The metric reflects a defining characteristic of large language models: output variability. When a task allows automatic verification, such as compiling or executing code, generating multiple candidates increases the likelihood that at least one will succeed. In that setting, variance becomes useful. In contrast, tasks that rely on human judgment, including creative writing or open-ended reasoning, expose the same variability as inconsistency rather than strength. The usefulness of stochastic generation therefore depends heavily on the evaluation environment. 

Language Models are Few-Shot Learners (Brown et al.) 

The paper Language Models are Few-Shot Learners by Brown et al. (2020) laid the groundwork for contemporary large language model research. It introduced GPT-3 and demonstrated that a sufficiently large model can adapt to new tasks directly at inference time, without gradient updates. The authors referred to this capability as in-context learning. 

 

 

 

Framework and Scaling 

 
Figure 16 

 
Figure 1.1 (Page 3) presents the meta-learning interpretation of the model. During large-scale pre-training, the system acquires general linguistic and task-related patterns. At inference time, it uses the prompt as a temporary training signal within the context window. No parameters change; adaptation occurs through pattern completion conditioned on the provided examples. 

 

Figure 17 

Scaling Results: Figure 1.2 (Page 4) compares models of different sizes and shows that larger systems extract more benefit from additional prompt examples. The improvement per example grows with scale, indicating that parameter count directly influences how effectively a model leverages contextual demonstrations. 

 

Figure 18 

Aggregate Performance: Figure 1.3 (Page 5) aggregates performance across 42 benchmarks. Zero-shot performance increases linearly with scale, but few-shot performance grows at a faster rate. This pattern proposes that the ability to infer task structure from examples strengthens disproportionately as models become larger. 

 

Computational Scale  

Table D.1 (Page 46) reports that training GPT-3 with 175 billion parameters required approximately 3.14 × 10²³ FLOPs. This marked a substantial increase over earlier transformer models such as RoBERTa and T5. The scale of computation strengthened what later became known as the scaling hypothesis: expanding model size, data volume, and training compute continues to produce measurable performance gains. 

 

The Few-Shot Paradigm 

Before GPT-3, most NLP systems followed a “pre-train then fine-tune” workflow. Brown et al. demonstrated that a large enough model could shift this paradigm toward “pre-train then prompt.” Instead of collecting labeled datasets and running task-specific optimization, users could define tasks through natural language instructions and examples. This decreased the cost of deployment and widened access to advanced NLP capabilities. 

 

At the same time, the prompting interface often produced unstable or misaligned outputs. Later work on instruction tuning and reinforcement learning from human feedback sought to address these constraints, refining the interaction model that GPT-3 introduced. 

 

 

 

Synthesis of Trends and Strategic Implications 

 

The cross-analysis of these foundational reveals a clear arc in the development of large language models. The field has not moved randomly from one technique to another. Instead, it has progressed through identifiable phases, each redefining what “improvement” means. Three broad trends stand out. 

 

The Efficiency Frontier: From Parameter Scaling to Data Scaling 

The transition from Brown et al. (2020) to Ouyang et al. (2022) marks a shift in how researchers measure efficiency. 

Era 1 (Scaling): Brown et al. established that parameter count (109 -> 1011) unlocks raw capability. Early large-model research concentrated on parameter growth. Moving from billions to hundreds of billions of parameters unlocked capabilities that smaller systems could not demonstrate. The central question during this period was simple: can the model perform the task at all? 

Era 2 (Alignment): Ouyang et al. proved that alignment data (RLHF) has a radically higher information density than pre-training data.  

Later work showed that not all data contributes equally to performance. Reinforcement Learning from Human Feedback introduced highly curated preference data into the training loop. A 1.3B InstructGPT model outperforming a 175B GPT-3 model suggests that targeted alignment data carries far more task-relevant signal than raw web-scale corpora. Large unaligned systems devote much of their capacity to modeling distributions that users never need. 

Implication: Future progress will likely depend less on expanding hardware and more on refining datasets. Carefully constructed human feedback, synthetic data pipelines, and domain-specific corpora might be able to provide higher returns than simply increasing parameter count. The Chinchilla results reinforce this interpretation by showing that many models were undertrained relative to their size, indicating that compute allocation and data quality interact directly with scale. 

The Nature of Reasoning: Logic vs. Structure 

The juxtaposition of Wang et al. (2023) and Marvin et al. (2024) offers a profound insight into the "mind" of the LLM. Wang et al.'s finding that models perform equally well with invalid logical steps suggests that LLMs are not "reasoning" in a symbolic sense. Instead, they are performing structural pattern matching. They recognize the shape of a logical argument (Premise $\rightarrow$ Step $\rightarrow$ Conclusion) and fill it with semantically appropriate content. 

Implication: This validates the "Prompt Engineering" framework proposed by Marvin et al. The goal of a prompt is not to "teach" the model logic, but to provide the correct template for the model to pour its knowledge into. If the template is correct (context, format, indicators), the model's internal probability distribution will handle the rest. 

The Crisis of Evaluation and the Rise of Agents 

The survey by Ni et al. (2025) and the psychometrics of Serapio-Garcia et al. (2025) highlight a widening gap between capability and verification. Model performance proceeds to grow, yet traditional standards struggle to keep up. 

 

Metric Failure: Static multiple-choice benchmarks, such as MMLU, face problems of memorization and dataset contamination. Accuracy alone fails to capture behavioral reliability or robustness in real-world deployment. 

New Standards: New benchmarks measure traits such as safety compliance, tool usage, and consistency across contexts. Psychometric approaches shows concepts like internal reliability (for example, alpha thresholds near 0.70) to assess whether a model’s “personality” remains stable across tasks. Evaluation increasingly resembles performance appraisal rather than exam scoring. 

Agentic Future: The explosion of agent benchmarks in 2024-2025 (Figure 1 in Ni et al.) signals the next phase: models that do things. This requires dynamic, "Google-proof" evaluations (like LiveBench) because an agent that memorizes the answer to "how to book a flight" is useless if it cannot interact with a live, changing airline API.  

Summary of RRL 

This report reviewed key metadata drawn from foundational papers in the Large Language Model era. It traces the field from early discussions of emergence at around 10^22 FLOPs to later alignment advances, where RLHF cut hallucination rates by roughly half. Taken together, the evidence shows a shift from systems driven mainly by statistical pattern matching toward models that are more structured, aligned with human preferences, and capable of acting in more agent-like ways. 

The literature also makes a consistent point. Scaling provides the raw capability, but alignment methods such as RLHF and structural techniques like prompt engineering and chain-of-thought guidance determine how usable that capability becomes. Some findings remain counterintuitive. Studies show that logically flawed intermediate steps can still help reasoning performance, and that smaller aligned models can outperform larger ones that lack alignment. These results suggest that researchers still do not fully understand how these systems work internally. Progress going forward will depend on stronger evaluation methods, including benchmarks designed with rigorous psychometric standards, so that reliability keeps pace as models continue scaling toward trillions of parameters. 

 

 

Methodology 

This chapter explains the experimental setup, how the data was collected, and the procedures used to test how prompt engineering affects code correctness. 

Experimental Protocols 

To ensure reliability and reproducibility, this study follows a strict two-stage automated protocol. 

Protocol 1: Automated Data Acquisition 

The Ground Truth dataset, GSM8K, is gathered entirely through automated steps to avoid manual selection bias. 
  

Structured Querying: Python scripts interface with the Hugging Face Datasets Hub using SQL-based querying to retrieve specific test cases. 

Immutable Retrieval: The “Question” and “Ground Truth Answer” are extracted exactly as they appear in the source repository to preserve the integrity of the evaluation standard. 

Protocol 2: Model Selection 

GPT-4o (OpenAI): The researchers considered this model as a baseline because its large-scale systems are trained with RLHF as well. 

Claude 3.5 Sonnet (Anthropic): This model has been included because it focuses strongly on safety constraints and Constitutional AI principles. 

Gemini 1.5 Pro (Google): Selected for Long-Context capabilities. 

Llama 3.1 (Meta): A considered model for its capability of handling long context inputs effectively. 

DeepSeek-Coder-V2: The study included it because its Mixture of Experts design focuses specifically on coding tasks. 

 

The researchers then ran the extracted prompts across all five models. Ni et al. (2025) describe these systems as representative examples of current state of the art LLM architectures. 

 

Testing Methods 

The testing phase follows established empirical approaches to measure how effective each prompt strategy is. 

LLM as a Judge 

Evaluating code logic cannot rely on simple string matching alone, so the study uses GPT 4 as an automated evaluator. 

Process: Each model’s generated code is provided to GPT 4 together with the original problem and the expected solution requirements. 

Rubric: GPT 4 scores the outputs based on functional correctness, time complexity considerations, and how well edge cases are handled. This approach follows earlier work showing that LLM based judging can produce reliable evaluations.4 

Confusion Matrix Analysis 

To statistically treat the results, a Confusion Matrix is employed to categorize the "Judge's" evaluations against the Ground Truth benchmarks. 

True Positive (TP): The model generated correct code, and the Judge evaluated it as correct. 

False Positive (FP): The model generated incorrect code, but the Judge falsely identified it as correct (Hallucination acceptance). 

True Negative (TN): The model generated incorrect code, and the Judge correctly identified it as incorrect. 

False Negative (FN): The model generated correct code, but the Judge falsely rejected it. 
This statistical treatment allows for the calculation of Precision, Recall, and F1-Scores for each prompting strategy (Zero-shot vs. Chain-of-Thought). 

Ablation Testing 

Adopted from Wang et al. (2023), ablation testing is performed by systematically removing components of the prompt (e.g., removing the "context" or "constraints" section) to measure the specific impact of each prompt engineering element on the final code performance . 

 

References 

1 T. Brown et al., "Language Models are Few-Shot Learners," Advances in Neural Information Processing Systems, 2020. 

2 L. Ouyang et al., "Training Language Models with Human Feedback," arXiv preprint arXiv:2203.02155, 2022. 

3 J. Wei et al., "Emergent Abilities of Large Language Models," Transactions on Machine Learning Research, 2022. 

4 J. Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS, 2022. 

S. M. Xie, A. Raghunathan, P. Liang, and T. Ma, "An Explanation of In-context Learning as Implicit Bayesian Inference," in International Conference on Learning Representations (ICLR), 2022. 

Y. Zhang, F. Zhang, Z. Yang, and Z. Wang, "What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization," in Proceedings of The 28th International Conference on Artificial Intelligence and Statistics, 2025. 

G. Serapio-García et al., "Personality Traits in Large Language Models," arXiv preprint arXiv:2307.00184, 2025. 

P. Liu et al., "Pre-train, Prompt, and Predict: A Survey of Prompt Engineering," ACM Computing Surveys, 2023. 

G. Marvin, N. Hellen, D. Jjingo, and J. Nakatumba-Nabende, "Prompt Engineering in Large Language Models," in Data Intelligence and Cognitive Informatics, Springer, 2024, pp. 387-402. 

B. Wang et al., "Towards Understanding Chain-of-Thought Prompting: An Empirical Study of What Matters," Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics, 2023, pp. 2717–2739. 

C. Donahue, M. Lee, and P. Liang, "Enabling language models to fill in the blanks," Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 2020, pp. 2492–2501. 

M. Chen et al., "Evaluating Large Language Models Trained on Code," arXiv preprint arXiv:2107.03374, 2021. 

S. Ni et al., "A Survey on Large Language Model Benchmarks," arXiv preprint arXiv:2508.15361, 2025. 

Works cited 

2508.15361v1.pdf 

In-Context Learning through the Bayesian Prism - arXiv, accessed February 13, 2026, https://arxiv.org/html/2306.04891v2 

The Mystery of In-Context Learning: A Comprehensive Survey on Interpretation and Analysis - ACL Anthology, accessed February 13, 2026, https://aclanthology.org/2024.emnlp-main.795.pdf 

In-Context Learning Is Provably Bayesian Inference: A Generalization Theory for Meta-Learning | OpenReview, accessed February 13, 2026, https://openreview.net/forum?id=dUwXJTF8kQ 

Rupak Sarkar, Bahareh Sarrafzadeh, Nirupama Chandrasekaran, Nagu Rangan, Philip Resnik, Longqi Yang, & Sujay Kumar Jauhar. (2025). Conversational User-AI Intervention: A Study on Prompt Rewriting for Improved LLM Response Generation. https://arxiv.org/abs/2503.16789  

 
    
    """

    metrics, meaning = analyze_text(text)

    print("\n=== NUMERICAL METRICS ===")
    for k,v in metrics.items():
        print(k, ":", v)

    print("\n=== INTERPRETATION ===")
    for k,v in meaning.items():
        print(k, ":", v)