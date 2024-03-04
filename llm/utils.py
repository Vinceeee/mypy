from langchain_community.llms.llamacpp import LlamaCpp
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.language_models.llms import LLM

class MyOwnLLM(LLM):
    pass


def main():
    template = """Question: {question}

    Answer: Let's work this out in a step by step way to be sure we have the right answer."""

    prompt = PromptTemplate.from_template(template)

    # Make sure the model path is correct for your system!
    llm = LlamaCpp(
        model_path="/home/tang/.cache/huggingface/hub/models--google--gemma-2b/snapshots/9d067f00def958594aaa16b39a65b07d69ca655b/gemma-2b.gguf",
        temperature=0.75,
        max_tokens=2000,
        top_p=1,
        verbose=True,  # Verbose is required to pass to the callback manager
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
    llm_chain.invoke(question)


if __name__ == "__main__":
    main()
