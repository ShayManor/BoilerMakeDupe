# SmithAI

## Inspiration
We were inspired by a challenge from Y Combinator to make AI more accessible for everyone. Rather than limiting powerful AI tools to those who can navigate a terminal or write code, we saw an opportunity to democratize AI. Our project extends this mission by enabling anyone—even complete beginners—to harness AI for complex tasks on demand, opening up possibilities that were once reserved for highly technical users.

## What It Does
SmithAI enables you to create and deploy AI “agents” tailored to your specific needs—be it answering questions, automating tasks, or analyzing data. Under the hood, an intelligent algorithm determines which large language model (LLM) is best suited for your request and seamlessly routes you there. No more second-guessing which AI tool to use—SmithAI handles the complexity behind the scenes.

## How We Built It
- **Full-Stack**: We developed a frontend using **HTML**, **JavaScript**, and **Tailwind CSS**, and integrated it with ChatGPT, Ollama, Deepseek, and Claude on the backend.  
- **Smart Routing Algorithm**: Our core logic evaluates multiple LLMs and dynamically chooses which one to use for a given query.  
- **App Store & Hosting**: We created our own app store on **MongoDB** and host each app on **AWS EC2**, utilizing **Elastic Beanstalk** for orchestration and **S3** for storage.  
- **Scalable AI**: We run smaller AI models directly on EC2 instances, balancing performance with cost-effectiveness.

## Challenges We Ran Into
1. **Model Orchestration**: Coordinating multiple AI models with different strengths and limitations required robust infrastructure planning and fallback mechanisms.  
2. **User-Friendly Interface**: Building an interface that’s intuitive for non-technical users while still offering advanced features for power users was a delicate balance.

## Accomplishments That We’re Proud Of
- **On-Demand AI Agents**: Users can spin up AI-driven agents without writing a single line of code.  
- **Seamless Model Switching**: Our intelligent routing algorithm automatically picks the best model for each request—no manual intervention needed.  
- **Infrastructure Mastery**: We’ve built a cohesive stack using EC2, Elastic Beanstalk, and S3 that easily scales as demand grows.

## What We Learned
- **Orchestration & Engineering**: Integrating multiple AI models is as much about system design as it is about AI expertise.  
- **Leveraging Strengths**: We learned how to blend the capabilities of different models (e.g., ChatGPT for natural language and Claude for complex reasoning) into one unified experience.  
- **Full-Stack & AWS**: Working with AWS EC2, Elastic Beanstalk, and S3 gave us hands-on experience in managing dynamic model selection and performance metrics.

## What's Next for SmithAI
- **Expand Model Library**: Incorporate specialized AI models for code generation, image recognition, and data analytics.  
- **User-Friendly Interface**: Continue to refine our UI/UX so anyone can deploy advanced AI without feeling overwhelmed.  
- **Enhanced Collaboration**: Add collaborative features for teams to build and share AI agents seamlessly.  
- **Global Accessibility**: Implement multi-language support and pursue partnerships to serve diverse communities worldwide.

By lowering the barrier to entry for AI, we believe SmithAI can spark new innovation across industries and empower users from all backgrounds. The possibilities are endless, and we’re excited to see how this technology evolves.
