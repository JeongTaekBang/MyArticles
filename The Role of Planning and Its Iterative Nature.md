![JN_20241025.png](media/JN_20241025.png)

# The Role of Planning and Its Iterative Nature

In both personal and professional life, setting a clear goal acts as a guidepost, helping us identify where we are and where we need to go. With a well-defined goal, we can measure our progress and make necessary adjustments along the way. 

However, while the **goal remains constant**, the **plans to achieve it should be flexible**. Just as in programming, where loops are used to iterate and improve, our plans must adapt to new information or unexpected changes, while still working towards the same ultimate goal. Each iteration brings us closer to success by refining our approach based on feedback. 

This iterative approach also applies to technical fields like machine learning. In machine learning, an initial model is trained on data and goes through cycles of feedback and adjustment, similar to refining plans in life. Each training cycle, or epoch, gathers performance metrics to help refine the model, moving closer to the target performance level.

Whether setting personal goals or training machine learning models, **flexible planning** and **consistent goals** are central to achieving success.


## Pseudo Code Representation of an Iterative Planning Process

```pseudo
BEGIN
    SET goal = "Target outcome"
    SET plan = "Initial roadmap"

    WHILE goal != achieved DO
        EXECUTE plan
        IF result == satisfactory THEN
            CONTINUE
        ELSE
            ADJUST plan based on feedback
        END IF
    END WHILE

    PRINT "Goal reached"
END
```

## Machine Learning Iterative Process: Pseudo Code

```pseudo
# Model Initialization
INITIALIZE model                             # 모델 초기화
SET max_epochs = 100                         # 최대 에포크 설정
SET learning_rate = 0.01                     # 학습률 설정
SET tolerance = 0.001                        # 허용 오차 설정
SET best_performance = None                  # 초기 최적 성능값

FOR each epoch:                              # 에포크 반복 (최대 100회)
    
    FOR each batch of data:                  # 배치 단위 학습 반복
        - Forward pass: Make predictions using the model           # 모델을 사용해 예측 수행
        - Calculate loss (difference between prediction and actual value)  # 손실 계산
        - Backward pass: Calculate gradients (adjustment amounts)          # 역전파 수행
        - Update model parameters using gradients and learning rate        # 파라미터 업데이트
    END FOR                                  # 배치 학습 종료

    # Model Evaluation
    Evaluate model on validation data                         # 에포크 종료 후 성능 평가
    IF best_performance is None OR performance improves:     # 성능이 향상된 경우
        - Save model (checkpoint)                            # 모델 저장 (체크포인트)
        - best_performance = performance                     # 최적 성능 업데이트
    ELSE:                                                    # 성능이 향상되지 않은 경우
        - Adjust learning rate or model parameters           # 학습률 또는 파라미터 조정
    END IF

    # Convergence Check
    IF performance < tolerance:                              # 허용 오차 이하로 성능이 도달한 경우
        PRINT "Model has converged"                          # 학습 종료 메시지
        BREAK                                                # 반복 종료
    END IF

END FOR                                                      # 전체 에포크 반복 종료

# Final Model Testing
EVALUATE model on test data                                  # 테스트 데이터에서 모델 최종 성능 평가
PRINT "Final model performance"                              # 최종 성능 출력
```

# Example: Achieving Fluency in English Conversation through Iterative Planning and Self-Feedback

### Goal
To achieve fluency in English conversation, enabling effective communication in a variety of social and professional contexts.

### Detailed Plan

This goal can be broken down into manageable steps with a focus on self-feedback for continuous improvement. Here’s a suggested approach:

---

## 1. Break Down the Goal

   - **Phase 1: Basic Vocabulary and Phrases**
     - Focus on learning essential vocabulary and commonly used phrases in everyday conversation (e.g., greetings, small talk, introductions).
     - Aim to learn 10-15 phrases per week, concentrating on pronunciation and meaning.
   
   - **Phase 2: Sentence Formation and Simple Conversations**
     - Practice constructing sentences using the vocabulary learned in Phase 1.
     - Engage in basic self-dialogue exercises, such as describing daily routines or talking about simple topics like hobbies and interests.
   
   - **Phase 3: Expanding Topics and Confidence Building**
     - Expand to more diverse topics (e.g., describing work, sharing opinions on general topics).
     - Practice holding a one-minute conversation on a single topic, gradually increasing to two or three minutes.
   
   - **Phase 4: Complex Conversations and Fluency Development**
     - Work on more complex sentence structures and topics (e.g., discussing news, explaining processes, or debating viewpoints).
     - Aim to sustain a conversation for five minutes or more, simulating real-life situations.
   
   - **Phase 5: Refinement and Accent Reduction**
     - Fine-tune pronunciation, work on reducing any noticeable accent if desired, and aim to speak with natural intonation.
     - Practice conversational responses to common questions in both social and professional settings.

---

## 2. Execution and Self-Feedback

The execution phase involves daily practice and a structured self-feedback system to continuously improve speaking skills.

1. **Daily Practice (10-15 minutes per day)**:
   - Start with brief, focused sessions that align with each phase’s objectives.
   - Use language learning apps or online resources to access audio clips and mimic pronunciation.

2. **Self-Recording and Playback**:
   - Record yourself speaking each day. This could be a simple phrase, a sentence, or a one-minute speech depending on the current phase.
   - Listen to the recording to identify areas that need improvement, such as pronunciation, fluency, or intonation.

3. **Self-Assessment and Reflection**:
   - After each recording, rate your performance on a scale (e.g., 1-5) in areas such as clarity, fluency, and naturalness.
   - Take notes on specific areas to focus on in the next practice session (e.g., "work on 'th' sounds," "pause less between sentences").

4. **Weekly Review and Goal Adjustment**:
   - At the end of each week, review progress by listening to a few recordings from the week.
   - Adjust focus for the next week based on identified strengths and weaknesses. For example, if pronunciation is improving but fluency is lacking, spend more time on fluid sentence formation.

5. **Milestone Celebrations**:
   - Celebrate reaching each phase to stay motivated. For example, reward yourself after successfully holding a conversation for three minutes without significant pauses.

---

## Pseudo Code for Iterative English Conversation Improvement with Self-Feedback

```pseudo
BEGIN
    SET goal = "Achieve fluency in English conversation"
    SET plan = ["Practice daily", "Record and assess", "Adjust focus as needed"]
    SET phases = ["Basic Vocabulary", "Sentence Formation", "Expanding Topics", "Complex Conversations", "Refinement"]
    SET milestones = ["Basic phrases", "Simple conversations", "Confident conversations", "Complex discussions", "Accent refinement"]

    FOR each phase IN phases DO
        WHILE milestone != achieved DO
            EXECUTE practice_step(phase)
            RECORD self_conversation
            SELF_ASSESS recording for clarity, fluency, intonation
            IF assessment < satisfactory THEN
                ADJUST focus area based on feedback
            ELSE
                CONTINUE practice in current phase
            END IF
            
            IF weekly_progress == satisfactory THEN
                UPDATE milestone_status
                IF milestone_status == achieved THEN
                    CELEBRATE milestone
                END IF
            END IF
        END WHILE
    END FOR

    PRINT "Fluency in English conversation achieved!"
END
```



# Example: Creating and Implementing an Investment Policy Statement (IPS) for Retirement Savings

### Goal
The primary objective of this IPS is to establish a structured plan for accumulating adequate retirement savings. This document defines the financial goals, risk tolerance, constraints, and asset allocation strategy that will guide investment decisions, with a focus on long-term growth and capital preservation.

---

## Key Components of the IPS

1. **Financial Goal**:
   - The main objective is to accumulate sufficient funds to support a comfortable retirement. This requires a balance between capital growth and risk management to preserve wealth over the long term.

2. **Risk Tolerance**:
   - The investor’s risk tolerance is moderate, willing to accept short-term volatility in exchange for long-term gains but prioritizing stability as retirement approaches.

3. **Investment Constraints**:
   - **Liquidity**: Minimal liquidity is required, as retirement funds will not be accessed until the retirement date.
   - **Time Horizon**: The time horizon is long-term, spanning 20+ years until retirement, allowing for growth-oriented investments.
   - **Tax Considerations**: Tax efficiency is essential; tax-deferred accounts or tax-advantaged investment vehicles should be utilized to minimize tax liabilities.
   - **Legal/Regulatory**: Investments should comply with applicable regulations for retirement accounts, including contribution limits and early withdrawal penalties.

4. **Asset Allocation**:
   - Based on the above factors, a diversified portfolio with a growth focus is appropriate. The portfolio will consist of stocks, bonds, and a small cash component to manage short-term volatility.

---

### Implementation and Review

1. **Portfolio Implementation**:
   - The initial portfolio will be constructed with a focus on growth-oriented assets (e.g., equity funds), complemented by fixed-income investments to provide stability.

2. **Periodic Review and Rebalancing**:
   - The portfolio will be reviewed annually to ensure alignment with the retirement savings goal. Rebalancing will be conducted if the asset allocation deviates significantly from the target allocation or if there is a material change in the investor’s financial situation.

---

## Pseudo Code Representation of the IPS Creation and Management Process

```pseudo
BEGIN
    # Step 1: Define Financial Goal
    SET financial_goal = "Accumulate sufficient retirement funds"

    # Step 2: Assess Risk Tolerance
    SET risk_tolerance = "Moderate"  # Willing to accept some volatility

    # Step 3: Identify Investment Constraints
    SET liquidity_needs = "Low"                     # Minimal liquidity required
    SET time_horizon = "Long-term (20+ years)"      # Long time horizon allows for growth focus
    SET tax_considerations = "Tax-efficient"        # Emphasis on tax-advantaged accounts
    SET legal_constraints = ["Retirement account regulations"]

    # Step 4: Define Asset Allocation based on Goals and Constraints
    IF risk_tolerance == "Moderate" THEN
        SET asset_allocation = {"Stocks": 70%, "Bonds": 25%, "Cash": 5%}
    ELSE
        SET asset_allocation = {"Stocks": 50%, "Bonds": 40%, "Cash": 10%}
    END IF

    # Step 5: Implement Portfolio
    EXECUTE investment_plan(asset_allocation)

    # Step 6: Review and Rebalance Periodically
    WHILE financial_goal != achieved DO
        ASSESS_PORTFOLIO(performance, market_conditions)
        
        IF portfolio_deviation > threshold THEN
            REBALANCE_PORTFOLIO(asset_allocation)
        END IF

        IF investor_situation_changed THEN
            UPDATE financial_goal, risk_tolerance, investment_constraints
            REDEFINE asset_allocation based on updated factors
        END IF
    END WHILE

    PRINT "Retirement savings goal achieved."
END
```
## IPS Example Breakdown

- **Financial Goal**: Accumulate a sufficient retirement fund for a comfortable lifestyle post-retirement.
- **Risk Tolerance**: Moderate, balancing growth potential with stability as the retirement date approaches.
- **Investment Constraints**:
  - **Liquidity**: Minimal liquidity needs since funds are not needed until retirement.
  - **Time Horizon**: Long-term (20+ years), allowing for growth-oriented investments.
  - **Tax Considerations**: Utilize tax-advantaged accounts to minimize tax liabilities.
  - **Legal/Regulatory**: Comply with retirement account regulations, including contribution limits and early withdrawal penalties.
- **Asset Allocation**: Growth-oriented allocation with a balance of:
  - **Stocks**: 70%
  - **Bonds**: 25%
  - **Cash**: 5%
- **Implementation and Review**:
  - Initial portfolio is implemented based on the defined allocation.
  - Annual reviews and rebalancing are conducted as needed to maintain alignment with the target allocation and respond to any changes in the investor’s financial situation or market conditions.

