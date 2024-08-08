// @generated by Thrift for thrift/compiler/test/fixtures/rust-skip-none-serialization/src/module.thrift
// This file is probably not the place you want to edit!

//! Server definitions for `module`.

#![recursion_limit = "100000000"]
#![allow(non_camel_case_types, non_snake_case, non_upper_case_globals, unused_crate_dependencies, unused_imports, clippy::all)]


#[doc(inline)]
pub use :: as types;

pub mod errors {
    #[doc(inline)]
    pub use ::::services::my_service;
    #[doc(inline)]
    #[allow(ambiguous_glob_reexports)]
    pub use ::::services::my_service::*;
}

pub(crate) use crate as server;
pub(crate) use ::::services;


#[::async_trait::async_trait]
pub trait MyService: ::std::marker::Send + ::std::marker::Sync + 'static {
    async fn ping(
        &self,
    ) -> ::std::result::Result<(), crate::services::my_service::PingExn> {
        ::std::result::Result::Err(crate::services::my_service::PingExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "MyService",
                "ping",
            ),
        ))
    }
    async fn getRandomData(
        &self,
    ) -> ::std::result::Result<::std::string::String, crate::services::my_service::GetRandomDataExn> {
        ::std::result::Result::Err(crate::services::my_service::GetRandomDataExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "MyService",
                "getRandomData",
            ),
        ))
    }
    async fn hasDataById(
        &self,
        _id: ::std::primitive::i64,
    ) -> ::std::result::Result<::std::primitive::bool, crate::services::my_service::HasDataByIdExn> {
        ::std::result::Result::Err(crate::services::my_service::HasDataByIdExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "MyService",
                "hasDataById",
            ),
        ))
    }
    async fn getDataById(
        &self,
        _id: ::std::primitive::i64,
    ) -> ::std::result::Result<::std::string::String, crate::services::my_service::GetDataByIdExn> {
        ::std::result::Result::Err(crate::services::my_service::GetDataByIdExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "MyService",
                "getDataById",
            ),
        ))
    }
    async fn putDataById(
        &self,
        _id: ::std::primitive::i64,
        _data: ::std::string::String,
    ) -> ::std::result::Result<(), crate::services::my_service::PutDataByIdExn> {
        ::std::result::Result::Err(crate::services::my_service::PutDataByIdExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "MyService",
                "putDataById",
            ),
        ))
    }
    async fn lobDataById(
        &self,
        _id: ::std::primitive::i64,
        _data: ::std::string::String,
    ) -> ::std::result::Result<(), crate::services::my_service::LobDataByIdExn> {
        ::std::result::Result::Err(crate::services::my_service::LobDataByIdExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "MyService",
                "lobDataById",
            ),
        ))
    }
}

#[::async_trait::async_trait]
impl<T> MyService for ::std::boxed::Box<T>
where
    T: MyService + Send + Sync + ?Sized,
{
    async fn ping(
        &self,
    ) -> ::std::result::Result<(), crate::services::my_service::PingExn> {
        (**self).ping(
        ).await
    }
    async fn getRandomData(
        &self,
    ) -> ::std::result::Result<::std::string::String, crate::services::my_service::GetRandomDataExn> {
        (**self).getRandomData(
        ).await
    }
    async fn hasDataById(
        &self,
        id: ::std::primitive::i64,
    ) -> ::std::result::Result<::std::primitive::bool, crate::services::my_service::HasDataByIdExn> {
        (**self).hasDataById(
            id,
        ).await
    }
    async fn getDataById(
        &self,
        id: ::std::primitive::i64,
    ) -> ::std::result::Result<::std::string::String, crate::services::my_service::GetDataByIdExn> {
        (**self).getDataById(
            id,
        ).await
    }
    async fn putDataById(
        &self,
        id: ::std::primitive::i64,
        data: ::std::string::String,
    ) -> ::std::result::Result<(), crate::services::my_service::PutDataByIdExn> {
        (**self).putDataById(
            id,
            data,
        ).await
    }
    async fn lobDataById(
        &self,
        id: ::std::primitive::i64,
        data: ::std::string::String,
    ) -> ::std::result::Result<(), crate::services::my_service::LobDataByIdExn> {
        (**self).lobDataById(
            id,
            data,
        ).await
    }
}

#[::async_trait::async_trait]
impl<T> MyService for ::std::sync::Arc<T>
where
    T: MyService + Send + Sync + ?Sized,
{
    async fn ping(
        &self,
    ) -> ::std::result::Result<(), crate::services::my_service::PingExn> {
        (**self).ping(
        ).await
    }
    async fn getRandomData(
        &self,
    ) -> ::std::result::Result<::std::string::String, crate::services::my_service::GetRandomDataExn> {
        (**self).getRandomData(
        ).await
    }
    async fn hasDataById(
        &self,
        id: ::std::primitive::i64,
    ) -> ::std::result::Result<::std::primitive::bool, crate::services::my_service::HasDataByIdExn> {
        (**self).hasDataById(
            id,
        ).await
    }
    async fn getDataById(
        &self,
        id: ::std::primitive::i64,
    ) -> ::std::result::Result<::std::string::String, crate::services::my_service::GetDataByIdExn> {
        (**self).getDataById(
            id,
        ).await
    }
    async fn putDataById(
        &self,
        id: ::std::primitive::i64,
        data: ::std::string::String,
    ) -> ::std::result::Result<(), crate::services::my_service::PutDataByIdExn> {
        (**self).putDataById(
            id,
            data,
        ).await
    }
    async fn lobDataById(
        &self,
        id: ::std::primitive::i64,
        data: ::std::string::String,
    ) -> ::std::result::Result<(), crate::services::my_service::LobDataByIdExn> {
        (**self).lobDataById(
            id,
            data,
        ).await
    }
}

/// Processor for MyService's methods.
#[derive(Clone, Debug)]
pub struct MyServiceProcessor<P, H, R, RS> {
    service: H,
    supa: ::fbthrift::NullServiceProcessor<P, R, RS>,
    _phantom: ::std::marker::PhantomData<(P, H, R, RS)>,
}

struct Args_MyService_ping {
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_MyService_ping {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "MyService.ping"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
        ];
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
        })
    }
}

struct Args_MyService_getRandomData {
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_MyService_getRandomData {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "MyService.getRandomData"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
        ];
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
        })
    }
}

struct Args_MyService_hasDataById {
    id: ::std::primitive::i64,
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_MyService_hasDataById {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "MyService.hasDataById"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
            ::fbthrift::Field::new("id", ::fbthrift::TType::I64, 1),
        ];
        let mut field_id = ::std::option::Option::None;
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (::fbthrift::TType::I64, 1) => field_id = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
            id: field_id.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "MyService.hasDataById", "id"))?,
        })
    }
}

struct Args_MyService_getDataById {
    id: ::std::primitive::i64,
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_MyService_getDataById {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "MyService.getDataById"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
            ::fbthrift::Field::new("id", ::fbthrift::TType::I64, 1),
        ];
        let mut field_id = ::std::option::Option::None;
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (::fbthrift::TType::I64, 1) => field_id = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
            id: field_id.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "MyService.getDataById", "id"))?,
        })
    }
}

struct Args_MyService_putDataById {
    id: ::std::primitive::i64,
    data: ::std::string::String,
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_MyService_putDataById {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "MyService.putDataById"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
            ::fbthrift::Field::new("data", ::fbthrift::TType::String, 2),
            ::fbthrift::Field::new("id", ::fbthrift::TType::I64, 1),
        ];
        let mut field_id = ::std::option::Option::None;
        let mut field_data = ::std::option::Option::None;
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (::fbthrift::TType::I64, 1) => field_id = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (::fbthrift::TType::String, 2) => field_data = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
            id: field_id.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "MyService.putDataById", "id"))?,
            data: field_data.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "MyService.putDataById", "data"))?,
        })
    }
}

struct Args_MyService_lobDataById {
    id: ::std::primitive::i64,
    data: ::std::string::String,
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_MyService_lobDataById {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "MyService.lobDataById"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
            ::fbthrift::Field::new("data", ::fbthrift::TType::String, 2),
            ::fbthrift::Field::new("id", ::fbthrift::TType::I64, 1),
        ];
        let mut field_id = ::std::option::Option::None;
        let mut field_data = ::std::option::Option::None;
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (::fbthrift::TType::I64, 1) => field_id = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (::fbthrift::TType::String, 2) => field_data = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
            id: field_id.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "MyService.lobDataById", "id"))?,
            data: field_data.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "MyService.lobDataById", "data"))?,
        })
    }
}


impl<P, H, R, RS> MyServiceProcessor<P, H, R, RS>
where
    P: ::fbthrift::Protocol + ::std::marker::Send + ::std::marker::Sync + 'static,
    P::Frame: ::std::marker::Send + 'static,
    P::Deserializer: ::std::marker::Send,
    H: MyService,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<P::Frame, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = <P as ::fbthrift::Protocol>::Frame>
        + ::std::marker::Send + ::std::marker::Sync,
    ::fbthrift::ProtocolDecoded<P>: ::std::clone::Clone,
    ::fbthrift::ProtocolEncodedFinal<P>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    pub fn new(service: H) -> Self {
        Self {
            service,
            supa: ::fbthrift::NullServiceProcessor::new(),
            _phantom: ::std::marker::PhantomData,
        }
    }

    pub fn into_inner(self) -> H {
        self.service
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "MyService.ping"))]
    async fn handle_ping<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"MyService";
        const METHOD_NAME: &::std::ffi::CStr = c"ping";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"MyService.ping";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_MyService_ping = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.ping(
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "MyService.ping", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::error!(method = "MyService.ping", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("MyService.ping", exn);
                ::tracing::error!(method = "MyService.ping", panic = ?aexn);
                ::std::result::Result::Err(crate::services::my_service::PingExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::my_service::PingExn>(
            "ping",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        ::std::result::Result::Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "MyService.getRandomData"))]
    async fn handle_getRandomData<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"MyService";
        const METHOD_NAME: &::std::ffi::CStr = c"getRandomData";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"MyService.getRandomData";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_MyService_getRandomData = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.getRandomData(
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "MyService.getRandomData", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::error!(method = "MyService.getRandomData", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("MyService.getRandomData", exn);
                ::tracing::error!(method = "MyService.getRandomData", panic = ?aexn);
                ::std::result::Result::Err(crate::services::my_service::GetRandomDataExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::my_service::GetRandomDataExn>(
            "getRandomData",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        ::std::result::Result::Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "MyService.hasDataById"))]
    async fn handle_hasDataById<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"MyService";
        const METHOD_NAME: &::std::ffi::CStr = c"hasDataById";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"MyService.hasDataById";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_MyService_hasDataById = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.hasDataById(
                _args.id,
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "MyService.hasDataById", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::error!(method = "MyService.hasDataById", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("MyService.hasDataById", exn);
                ::tracing::error!(method = "MyService.hasDataById", panic = ?aexn);
                ::std::result::Result::Err(crate::services::my_service::HasDataByIdExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::my_service::HasDataByIdExn>(
            "hasDataById",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        ::std::result::Result::Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "MyService.getDataById"))]
    async fn handle_getDataById<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"MyService";
        const METHOD_NAME: &::std::ffi::CStr = c"getDataById";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"MyService.getDataById";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_MyService_getDataById = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.getDataById(
                _args.id,
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "MyService.getDataById", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::error!(method = "MyService.getDataById", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("MyService.getDataById", exn);
                ::tracing::error!(method = "MyService.getDataById", panic = ?aexn);
                ::std::result::Result::Err(crate::services::my_service::GetDataByIdExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::my_service::GetDataByIdExn>(
            "getDataById",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        ::std::result::Result::Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "MyService.putDataById"))]
    async fn handle_putDataById<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"MyService";
        const METHOD_NAME: &::std::ffi::CStr = c"putDataById";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"MyService.putDataById";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_MyService_putDataById = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.putDataById(
                _args.id,
                _args.data,
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "MyService.putDataById", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::error!(method = "MyService.putDataById", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("MyService.putDataById", exn);
                ::tracing::error!(method = "MyService.putDataById", panic = ?aexn);
                ::std::result::Result::Err(crate::services::my_service::PutDataByIdExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::my_service::PutDataByIdExn>(
            "putDataById",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        ::std::result::Result::Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "MyService.lobDataById"))]
    async fn handle_lobDataById<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"MyService";
        const METHOD_NAME: &::std::ffi::CStr = c"lobDataById";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"MyService.lobDataById";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_MyService_lobDataById = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.lobDataById(
                _args.id,
                _args.data,
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "MyService.lobDataById", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::error!(method = "MyService.lobDataById", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("MyService.lobDataById", exn);
                ::tracing::error!(method = "MyService.lobDataById", panic = ?aexn);
                ::std::result::Result::Err(crate::services::my_service::LobDataByIdExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::my_service::LobDataByIdExn>(
            "lobDataById",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        ::std::result::Result::Ok(())
    }
}

#[::async_trait::async_trait]
impl<P, H, R, RS> ::fbthrift::ServiceProcessor<P> for MyServiceProcessor<P, H, R, RS>
where
    P: ::fbthrift::Protocol + ::std::marker::Send + ::std::marker::Sync + 'static,
    P::Deserializer: ::std::marker::Send,
    H: MyService,
    P::Frame: ::std::marker::Send + 'static,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = <P as ::fbthrift::Protocol>::Frame>
        + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<P::Frame, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    ::fbthrift::ProtocolDecoded<P>: ::std::clone::Clone,
    ::fbthrift::ProtocolEncodedFinal<P>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    type RequestContext = R;
    type ReplyState = RS;

    #[inline]
    fn method_idx(&self, name: &[::std::primitive::u8]) -> ::std::result::Result<::std::primitive::usize, ::fbthrift::ApplicationException> {
        match name {
            b"ping" => ::std::result::Result::Ok(0usize),
            b"getRandomData" => ::std::result::Result::Ok(1usize),
            b"hasDataById" => ::std::result::Result::Ok(2usize),
            b"getDataById" => ::std::result::Result::Ok(3usize),
            b"putDataById" => ::std::result::Result::Ok(4usize),
            b"lobDataById" => ::std::result::Result::Ok(5usize),
            _ => ::std::result::Result::Err(::fbthrift::ApplicationException::unknown_method()),
        }
    }

    #[allow(clippy::match_single_binding)]
    async fn handle_method(
        &self,
        idx: ::std::primitive::usize,
        _p: &mut P::Deserializer,
        _req: ::fbthrift::ProtocolDecoded<P>,
        _req_ctxt: &R,
        _reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        match idx {
            0usize => {
                self.handle_ping(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            1usize => {
                self.handle_getRandomData(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            2usize => {
                self.handle_hasDataById(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            3usize => {
                self.handle_getDataById(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            4usize => {
                self.handle_putDataById(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            5usize => {
                self.handle_lobDataById(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            bad => panic!(
                "{}: unexpected method idx {}",
                "MyServiceProcessor",
                bad
            ),
        }
    }

    #[allow(clippy::match_single_binding)]
    #[inline]
    fn create_interaction_idx(&self, name: &::std::primitive::str) -> ::anyhow::Result<::std::primitive::usize> {
        match name {
            _ => ::anyhow::bail!("Unknown interaction"),
        }
    }

    #[allow(clippy::match_single_binding)]
    fn handle_create_interaction(
        &self,
        idx: ::std::primitive::usize,
    ) -> ::anyhow::Result<
        ::std::sync::Arc<dyn ::fbthrift::ThriftService<P::Frame, Handler = (), RequestContext = Self::RequestContext, ReplyState = Self::ReplyState> + ::std::marker::Send + 'static>
    > {
        match idx {
            bad => panic!(
                "{}: unexpected method idx {}",
                "MyServiceProcessor",
                bad
            ),
        }
    }

    async fn handle_on_termination(&self) {
    }
}

#[::async_trait::async_trait]
impl<P, H, R, RS> ::fbthrift::ThriftService<P::Frame> for MyServiceProcessor<P, H, R, RS>
where
    P: ::fbthrift::Protocol + ::std::marker::Send + ::std::marker::Sync + 'static,
    P::Deserializer: ::std::marker::Send,
    P::Frame: ::std::marker::Send + 'static,
    H: MyService,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = <P as ::fbthrift::Protocol>::Frame>
        + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<P::Frame, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    ::fbthrift::ProtocolDecoded<P>: ::std::clone::Clone,
    ::fbthrift::ProtocolEncodedFinal<P>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    type Handler = H;
    type RequestContext = R;
    type ReplyState = RS;

    #[tracing::instrument(level="trace", skip_all, fields(service = "MyService"))]
    async fn call(
        &self,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
    ) -> ::anyhow::Result<()> {
        use ::fbthrift::{ProtocolReader as _, ServiceProcessor as _};
        let mut p = P::deserializer(req.clone());
        let (idx, mty, seqid) = p.read_message_begin(|name| self.method_idx(name))?;
        if mty != ::fbthrift::MessageType::Call {
            return ::std::result::Result::Err(::std::convert::From::from(::fbthrift::ApplicationException::new(
                ::fbthrift::ApplicationExceptionErrorCode::InvalidMessageType,
                format!("message type {:?} not handled", mty)
            )));
        }
        let idx = match idx {
            ::std::result::Result::Ok(idx) => idx,
            ::std::result::Result::Err(_) => {
                return self.supa.call(req, req_ctxt, reply_state).await;
            }
        };
        self.handle_method(idx, &mut p, req, req_ctxt, reply_state, seqid).await?;
        p.read_message_end()?;

        ::std::result::Result::Ok(())
    }

    fn create_interaction(
        &self,
        name: &::std::primitive::str,
    ) -> ::anyhow::Result<
        ::std::sync::Arc<dyn ::fbthrift::ThriftService<P::Frame, Handler = (), RequestContext = R, ReplyState = RS> + ::std::marker::Send + 'static>
    > {
        use ::fbthrift::{ServiceProcessor as _};
        let idx = self.create_interaction_idx(name);
        let idx = match idx {
            ::anyhow::Result::Ok(idx) => idx,
            ::anyhow::Result::Err(_) => {
                return self.supa.create_interaction(name);
            }
        };
        self.handle_create_interaction(idx)
    }

    fn get_method_names(&self) -> &'static [&'static ::std::primitive::str] {
        &[
            // From module.MyService:
            "ping",
            "getRandomData",
            "hasDataById",
            "getDataById",
            "putDataById",
            "lobDataById",
        ]
    }

    async fn on_termination(&self) {
        use ::fbthrift::{ServiceProcessor as _};
        self.handle_on_termination().await
    }
}

/// Construct a new instance of a MyService service.
///
/// This is called when a new instance of a Thrift service Processor
/// is needed for a particular Thrift protocol.
#[::tracing::instrument(level="debug", skip_all, fields(proto = ?proto))]
pub fn make_MyService_server<F, H, R, RS>(
    proto: ::fbthrift::ProtocolID,
    handler: H,
) -> ::std::result::Result<::std::boxed::Box<dyn ::fbthrift::ThriftService<F, Handler = H, RequestContext = R, ReplyState = RS> + ::std::marker::Send + 'static>, ::fbthrift::ApplicationException>
where
    F: ::fbthrift::Framing + ::std::marker::Send + ::std::marker::Sync + 'static,
    H: MyService,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = F> + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<F, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    ::fbthrift::FramingDecoded<F>: ::std::clone::Clone,
    ::fbthrift::FramingEncodedFinal<F>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    match proto {
        ::fbthrift::ProtocolID::BinaryProtocol => {
            ::std::result::Result::Ok(::std::boxed::Box::new(MyServiceProcessor::<::fbthrift::BinaryProtocol<F>, H, R, RS>::new(handler)))
        }
        ::fbthrift::ProtocolID::CompactProtocol => {
            ::std::result::Result::Ok(::std::boxed::Box::new(MyServiceProcessor::<::fbthrift::CompactProtocol<F>, H, R, RS>::new(handler)))
        }
        bad => {
            ::tracing::error!(method = "MyService.", invalid_protocol = ?bad);
            ::std::result::Result::Err(::fbthrift::ApplicationException::invalid_protocol(bad))
        }
    }
}
