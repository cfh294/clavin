# clavin
Simplified email for Python

```python
import clavin

with clavin.Mailman("localhost", 25) as email_client:
    email_client.deliver(
        from_address="john@eggs.com",
        to_list=["terry@spam.com", "michael@ham.com"],
        cc_list=["graham@spam.com"],
        bcc_list=["eric@eggs.com"],
        text="No one expects the Spanish Inquisition!",
        html="<h1>A fancier message</h1>",
        subject="Email Example"
    )
```

## Installation

Not ready yet!

## Dependencies 

Python>=3.8.5
