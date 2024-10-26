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