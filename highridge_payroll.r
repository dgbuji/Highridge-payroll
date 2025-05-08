generate_payslips <- function() {
    # Generate payslips for 400 employees at Highridge
    tryCatch(
        {
            # Dynamically create a list of 400 employees
            employees <- list()
            for (i in 1:400) {
                employee <- list(
                    id = i,
                    name = paste0("Employee_", i),
                    gender = sample(c("Male", "Female"), 1),
                    salary = sample(5000:35000, 1) # salary between $5,000 and $35,000
                )
                employees[[i]] <- employee
            }

            # Generate payslips for each employee
            for (employee in employees) {
                tryCatch(
                    {
                        # Conditional Employee Level Categorization
                        employee_level <- "Regular" # Default level
                        # Condition 1
                        if (employee$salary > 10000 && employee$salary < 20000) {
                            employee_level <- "A1"
                        }
                        # Condition 2
                        if (employee$salary > 7500 && employee$salary <
                            30000 && employee$gender == "Female") {
                            employee_level <- "A5-F"
                        }

                        # Printing Payslip
                        cat(
                            "\n=== Payment Slip for", employee$name,
                            "(ID:", employee$id, ") ===\n"
                        )
                        cat("Gender:", employee$gender, "\n")
                        cat("Salary:$", employee$salary, "\n")
                        cat("Employee_level:", employee_level, "\n")
                        cat(rep("-", 40), "\n")
                    },
                    error = function(e) {
                        cat("Error generating payslip for employee ID:", employee$id, "\n")
                        cat("Error message:", e$message, "\n")
                    }
                )
            }
        },
        error = function(e) {
            cat("Error generating payslips:", e$message, "\n")
        }
    )
}
# Call the function to generate payslips
generate_payslips()
