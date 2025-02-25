# totoroid-poc
Automated streaming (output only system)

driving questions:
- In what resolution, temporal consistency, and captivating narrative can the latest open source stable diffusion model generate when executing on enterprise level compute vs. consumer level compute?
- How much time is required for this generated video output to be **content-positive*** - (the stream is endless: has less frames leaving from memory into a **stream-output** than the average frames generated into memory for any given period of time)
- Can this content-positive automated stream-output earn the maximum number of **ERN*** - (eyes right now: the total number of users capable of consuming any **stream-output**)

# 1. collect most popular live stream data from youtube and finetune stable diffusion models at runtime, saving checkpoints when desired. (https://github.com/totoroidsai/generate-live-stream-dataset)
   **why?** live stream content is highly competative for ERN yet generally more static and convenient to train faster for stable diffusion
   
# 2. train by finetuning any stable diffusion model in RUNTIME => we want to capture the pixels from livestreams and while they are in memory, train the model, and then after enough time save the model checkpoint
   **why?** a deliberate choice to always have a changing training set since live content is always changing, we only need to get a sense of where we are in the evolutionary process of that content

# 3. generate unique agents for competition (https://github.com/totoroidsai/echomimic_crew_wrapper)
   **why?** some kind of mechanism to dynamically create agents that are motivated to survive relegation. This way we constantly foster competition among the individual streams.

# 4. inference output compiled into [content-positive stream-output] (https://github.com/totoroidsai/broadcast_stable_diffusion_output_continuously)

# 5. relegation
  **why?** A constant process to remove the consistently underperforming streams and replacing them with fresh perspective agents who can offer new solutions to survival.



![dl](https://github.com/user-attachments/assets/ad779774-7fac-4293-8b9b-66a541341465)
